from config import CfgNode as CN

# -----------------------------------------------------------------------------
# Config definition
# -----------------------------------------------------------------------------

_C = CN()

# The version number, to upgrade from old configs to new ones if any
# changes happen. It's recommended to keep a VERSION in your config file.
_C.VERSION = 2

_C.DEVICE = 'cuda'

_C.ENV = CN()
_C.ENV.NAME = 'Pong-v4'

_C.PATHS = CN()
_C.PATHS.OUTPUT_DIR = 'output'
_C.PATHS.CHECKPOINT = 'checkpoint.pong.pth'

_C.POLICY = CN()
_C.POLICY.FEATURE_EXTRACTION = True
_C.POLICY.NETWORK = CN()
_C.POLICY.NETWORK.NAME = 'resnet'
_C.POLICY.NETWORK.DEPTH = 18

_C.TRAINING = CN()
_C.TRAINING.BATCH_SIZE = 8
_C.TRAINING.EPISODES = 1000
_C.TRAINING.GAMMA = 0.75
_C.TRAINING.LR = 0.0001
_C.TRAINING.EPSILON = CN()
_C.TRAINING.EPSILON.START = 0.9
_C.TRAINING.EPSILON.END = 0.05
_C.TRAINING.EPSILON.DECAY = 200

_C.REPLAY_MEMORY = CN()
_C.REPLAY_MEMORY.SIZE = 10000

_C.TARGET = CN()
_C.TARGET.UPDATE_WEIGHTS = 10
_C.TARGET.NETWORK = CN()
_C.TARGET.NETWORK.NAME = 'resnet'
_C.TARGET.NETWORK.DEPTH = 18

_C.LOGGING = CN()
_C.LOGGING.LOGFILE = 'output.log'

# global config is for quick hack purposes.
# You can set them in command line or config files,
# and access it with:
#
# from detectron2.config import global_cfg
# print(global_cfg.HACK)
#
# Do not commit any configs into it.
_C.GLOBAL = CN()
_C.GLOBAL.HACK = 1.0