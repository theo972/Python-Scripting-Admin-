import psutil


def cpu_info():
    """
        Gather the info from the device's processor and returns it under dictionary form
    :return:
    """
    cpu = {
        'cpu_time': psutil.cpu_times().user,
        'cpu_percent': psutil.cpu_percent(interval=1),
    }

    return cpu


def memory_info():
    """
        Gather the info from the device's ram and returns it under dictionary form
    :return:
    """
    memory = {
        'virtual_memory_total': psutil.virtual_memory().total,
        'virtual_memory_available': psutil.virtual_memory().available,
        'virtual_memory_percent': psutil.virtual_memory().percent,
    }
    return memory


def disk_info():
    """
        Gather the info from the device's disk and returns it under dictionary form
    :return:
    """
    disk = {
        'disk_usage_percent': psutil.disk_usage('/').percent,
        'disk_usage_total': psutil.disk_usage('/').total,
        'disk_usage_used': psutil.disk_usage('/').used
    }
    return disk


def network_info():
    """
        Gather the info from the device's network and returns it under dictionary form
    :return:
    """
    network = {
        'net_counter_bytes_sent': psutil.net_io_counters(pernic=False, nowrap=True).bytes_sent,
        'net_counter_bytes_recv': psutil.net_io_counters(pernic=False, nowrap=True).bytes_recv,
    }
    return network


def sensor_info():
    """
        Gather the info from the device's sensor and returns it under dictionary form
    :return:
    """
    sensor = {
        'sensor_battery': psutil.sensors_battery().percent
    }
    return sensor
