import os
import logging

from glob import glob

from agent import Agent
from atari_pong import Pong
from policies import model_map
from environment import make_env
from optimizer import adam_optimizer
from replay_memory import ReplayMemory
from loss_functions import l1_loss, mse_loss
from utils.checkpoint import load_checkpoint
from utils.read_config import reading_config
from utils.setup_logging import setup_logging


logger = logging.getLogger('pong')

def main():

    #read config file
    config_file = None
    cfg = reading_config(config_file)

    #output directory
    dirs = glob(os.path.join(cfg.PATHS.OUTPUT_DIR, "run*"))
    if len(dirs):
        output_dir = os.path.join(cfg.PATHS.OUTPUT_DIR, f"run-{len(dirs)}")
    else:
        output_dir = os.path.join(cfg.PATHS.OUTPUT_DIR, f"run")
        
    os.makedirs(output_dir)


    #setup logging
    logfile_path = os.path.join(output_dir, "output.log")
    setup_logging(logfile=logfile_path)

    #environment
    env_name = cfg.ENV.NAME
    env = make_env(env_name)

    #configs
    batch_size = cfg.TRAINING.BATCH_SIZE
    episodes = cfg.TRAINING.EPISODES
    gamma = cfg.TRAINING.GAMMA
    learning_rate = cfg.TRAINING.LR
    epsilon_start = cfg.TRAINING.EPSILON.START
    epsilon_end = cfg.TRAINING.EPSILON.END
    epsilon_decay = cfg.TRAINING.EPSILON.DECAY
    feature_extraction = cfg.POLICY.FEATURE_EXTRACTION
    n_actions = env.action_space.n
    device = cfg.DEVICE
    target_update = cfg.TARGET.UPDATE_WEIGHTS

    policy_network = cfg.POLICY.NETWORK.NAME
    policy_depth = cfg.POLICY.NETWORK.DEPTH
    target_network = cfg.TARGET.NETWORK.NAME
    target_depth = cfg.TARGET.NETWORK.DEPTH

    # policy network
    policy_network = model_map[policy_network][policy_depth](n_actions, feature_extraction).to(device)
    
    # target network
    target_network = model_map[target_network][target_depth](n_actions, feature_extraction).to(device)
    
    # initializing the weights of target network
    target_network.load_state_dict(policy_network.state_dict())
    
    # freezing the target network's weights
    target_network.eval()

    # optimizer
    optimizer = adam_optimizer(policy_network, learning_rate)

    # loss function
    criterion = l1_loss

    # experience
    memory_size = cfg.REPLAY_MEMORY.SIZE
    memory = ReplayMemory(memory_size)

    # loading the checkpoint
    checkpoint_file = os.path.join(output_dir, cfg.PATHS.CHECKPOINT)
    checkpoint_pong = load_checkpoint(checkpoint_file, cfg.DEVICE)
    start_episode = 1
    if checkpoint_pong is not None:
        start_episode = checkpoint_pong['episode'] + 1
        policy_network.load_state_dict(checkpoint_pong['policy_net'])
        optimizer.load_state_dict(checkpoint_pong['optimizer'])
    del checkpoint_pong

    # agent
    agent = Agent(policy_network, n_actions)

    # model
    model = Pong(env, policy_network, target_network, agent, optimizer, criterion, memory, output_dir, cfg.DEVICE)

    # training
    model.train(episodes, target_update, start_episode, batch_size, epsilon_start, epsilon_end, epsilon_decay, gamma)
    # model.evalutate()


if __name__ == "__main__":
    main()