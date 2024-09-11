from rl.callbacks import ModelIntervalCheckpoint

def get_callback(filename, interval):
    return ModelIntervalCheckpoint(filename, interval=interval)