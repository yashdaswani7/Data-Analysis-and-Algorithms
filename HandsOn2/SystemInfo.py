import platform
import psutil

def get_system_info():
    print("System Information:")
    print(f"Processor: {platform.processor()}")
    print(f"RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
    print(f"System: {platform.system()} {platform.release()}")

get_system_info()
