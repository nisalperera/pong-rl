from .alexnet_policy import Alexnet
from .resnet_policy import Resnet18

model_map = {
    "resnet": {
        18: Resnet18
    },

    "alexnet": {
        0: Alexnet
    }
}