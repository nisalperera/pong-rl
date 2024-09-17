import psutil
import GPUtil


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    return memory_usage

def get_gpu_usage():
    gpus = GPUtil.getGPUs()
    gpu_usage = [gpu.load * 100 for gpu in gpus]
    return gpu_usage

def get_resourse_usage():
    return get_cpu_usage(), get_memory_usage(), get_gpu_usage()