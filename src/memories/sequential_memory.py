from rl.memory import SequentialMemory


def get_memory(limit, window_length):
    return SequentialMemory(limit=limit, window_length=window_length)