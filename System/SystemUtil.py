import psutil


# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def print_hi(name):
    print(f'Hi, {name}')


def cpu_info():
    cpu = {'cpu_time': psutil.cpu_times(),
           'cpu_percent': psutil.cpu_percent(interval=1),
           'cpu_stats': psutil.cpu_stats()}
    return cpu


def memory_info():
    memory = {'virtual_memory': psutil.virtual_memory(),
              'swap_memory': psutil.swap_memory()}
    return memory


def disk_info():
    disk = {'disk_partition': psutil.disk_partitions(all=False),
            'disk_usage': psutil.disk_usage('/'),
            'disk_counter': psutil.disk_io_counters()}
    return disk


def network_info():
    network = {'net_counter': psutil.net_io_counters(pernic=False, nowrap=True)}
    return network


def sensor_info():
    sensor = {'sensor_battery': psutil.sensors_battery()}
    return sensor
