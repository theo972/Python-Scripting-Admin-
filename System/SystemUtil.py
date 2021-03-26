import psutil


def cpu_info():
    """
        Gather the info from the device's cpu and returns it under dictionary form
    :return: cpu
    """
    cpu = {
        'cpu_time': psutil.cpu_times().user,
        'cpu_percent': psutil.cpu_percent(interval=1),
    }

    return cpu


def memory_info():
    """
         Gather the info from the device's memory and returns it under dictionary form
     :return: memory
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
      :return: disk
    """
    disk = {'disk_usage_percent': psutil.disk_usage('/').percent,
            'disk_usage_total': psutil.disk_usage('/').total,
            'disk_usage_used': psutil.disk_usage('/').used}

    return disk


def network_info():
    """

              Gather the info from the device's network and returns it under dictionary form
          :return: network
    """
    network = {
        'net_counter_bytes_sent': psutil.net_io_counters(pernic=False, nowrap=True).bytes_sent,
        'net_counter_bytes_recv': psutil.net_io_counters(pernic=False, nowrap=True).bytes_recv,
    }

    return network


def sensor_info():
    """
        Gather the info from the device's sensor and returns it under dictionary form
       :return: sensor
    """
    sensor = {'sensor_battery': psutil.sensors_battery().percent}

    return sensor
