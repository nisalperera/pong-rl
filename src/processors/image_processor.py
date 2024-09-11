import numpy as np

from rl.processors import Processor
from PIL import Image


class ImageProcessor(Processor):
    def process_observation(self, observation):
        IMG_SHAPE = (84, 84)
        
        img = Image.fromarray(observation)
        img = img.resize(IMG_SHAPE)
        img = img.convert("L")
        img = np.array(img)
        
        return img.astype(np.uint8)
    
    def process_state_batch(self, batch):
        return batch / 255.0
    
    def process_reward(self, reward):
        return np.clip(reward, -1.0, 1.0)
    
    
def get_processor():
    return ImageProcessor()