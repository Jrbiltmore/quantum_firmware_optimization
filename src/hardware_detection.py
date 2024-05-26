import psutil
import cpuinfo

def get_cpu_info():
    info = cpuinfo.get_cpu_info()
    return {
        "brand": info["brand_raw"],
        "hz_actual": info["hz_actual_friendly"],
        "arch": info["arch"],
        "bits": info["bits"],
        "count": psutil.cpu_count(logical=False),
        "logical_count": psutil.cpu_count(logical=True)
    }

def get_memory_info():
    mem = psutil.virtual_memory()
    return {
        "total": mem.total,
        "available": mem.available,
        "percent": mem.percent,
        "used": mem.used,
        "free": mem.free
    }

def get_disk_info():
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
    return disk_info

def get_firmware_version():
    try:
        result = subprocess.run(["dmidecode", "-t", "bios"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

def get_hardware_info():
    return {
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info(),
        "firmware": get_firmware_version()
    }