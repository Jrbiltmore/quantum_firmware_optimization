# quantum_firmware_optimization/src/hardware_detection.py

import psutil
import cpuinfo
import logging
import subprocess

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("hardware_detection.log"),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger(__name__)

def get_cpu_info():
    """
    Get information about the CPU.

    Returns:
        dict: A dictionary containing CPU information.
    """
    try:
        info = cpuinfo.get_cpu_info()
        cpu_info = {
            "brand": info["brand_raw"],
            "hz_actual": info["hz_actual_friendly"],
            "arch": info["arch"],
            "bits": info["bits"],
            "count": psutil.cpu_count(logical=False),
            "logical_count": psutil.cpu_count(logical=True)
        }
        logger.info(f"CPU info: {cpu_info}")
        return cpu_info
    except Exception as e:
        logger.error(f"Error getting CPU info: {e}")
        return {}

def get_memory_info():
    """
    Get information about the system memory.

    Returns:
        dict: A dictionary containing memory information.
    """
    try:
        mem = psutil.virtual_memory()
        memory_info = {
            "total": mem.total,
            "available": mem.available,
            "percent": mem.percent,
            "used": mem.used,
            "free": mem.free
        }
        logger.info(f"Memory info: {memory_info}")
        return memory_info
    except Exception as e:
        logger.error(f"Error getting memory info: {e}")
        return {}

def get_disk_info():
    """
    Get information about the disk partitions and usage.

    Returns:
        dict: A dictionary containing disk information for each partition.
    """
    try:
        disk_info = {}
        partitions = psutil.disk_partitions()
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info[partition.device] = {
                "total": usage.total,
                "used": usage.used,
                "free": usage.free,
                "percent": usage.percent
            }
        logger.info(f"Disk info: {disk_info}")
        return disk_info
    except Exception as e:
        logger.error(f"Error getting disk info: {e}")
        return {}

def get_firmware_version():
    """
    Get the firmware version of the system.

    Returns:
        str: The firmware version information.
    """
    try:
        result = subprocess.run(["dmidecode", "-t", "bios"], capture_output=True, text=True)
        firmware_version = result.stdout.strip()
        logger.info(f"Firmware version: {firmware_version}")
        return firmware_version
    except Exception as e:
        logger.error(f"Error getting firmware version: {e}")
        return str(e)

def get_hardware_info():
    """
    Get comprehensive hardware information of the system.

    Returns:
        dict: A dictionary containing comprehensive hardware information.
    """
    hardware_info = {
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info(),
        "firmware": get_firmware_version()
    }
    logger.info(f"Hardware info: {hardware_info}")
    return hardware_info

if __name__ == "__main__":
    logger.info("Starting hardware detection...")
    hardware_info = get_hardware_info()
    logger.info(f"Detected hardware info: {hardware_info}")
    print(hardware_info)
