import tensorflow
import keras
import rl

print(f"Tensorflow version: {tensorflow.__version__}")
print(f"Keras version: {keras.__version__}")

from envs import get_env
from memories import get_memory
from models import load_weights, get_callback, get_optimizer
from policies import get_policy
from processors import get_processor
from agents import get_agent


env = get_env()
nb_actions = env.action_space.n
processor = get_processor()
policy = get_policy()
model = load_weights((84, 84), nb_actions)
memory = get_memory(500000, 12)

dqn = get_agent(
    model, 
    nb_actions=nb_actions, 
    policy=policy, 
    memory=memory, 
    processor=processor, 
    nb_steps_warmup=50000,
    gamma=0.99,
    target_model_update=1000,
    train_interval=12,
    delta_clip=1    
)

dqn.compile(get_optimizer(lr=0.00025), metrics=['mae'])
callbacks = get_callback("checkpoint.hf5", interval=1000)

dqn.fit(env, nb_steps=1000000, callbacks=[callbacks], log_interval=10000, visualize=False)
dqn.test(env, nb_episodes=1, visualize=True)