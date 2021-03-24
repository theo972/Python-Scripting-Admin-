import psutil


# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def print_hi(name):
    print(f'Hi, {name}')


def cpu_info():
    cpu = {
        'cpu_time': psutil.cpu_times().user,
        'cpu_precent': psutil.cpu_percent(interval=1),
        'cpu_stats': psutil.cpu_stats().ctx_switches
    }

    return cpu


def memory_info():
    memory = {'virtual_memory_total': psutil.virtual_memory().total,
              'virtual_memory_available': psutil.virtual_memory().available,
              'virtual_memory_percent': psutil.virtual_memory().percent,
              }
    return memory


def disk_info():
    disk = {'disk_usage_percent': psutil.disk_usage('/').percent,
            'disk_usage_total': psutil.disk_usage('/').total,
            'disk_usage_used': psutil.disk_usage('/').used,
            'disk_counter_read_count': psutil.disk_io_counters().read_count,
            'disk_counter_write_count': psutil.disk_io_counters().write_count}
    return disk


def network_info():
    network = {'net_counter_bytes_sent': psutil.net_io_counters(pernic=False, nowrap=True).bytes_sent,
               'net_counter_bytes_recv': psutil.net_io_counters(pernic=False, nowrap=True).bytes_recv,
               'net_counter_packets_sent': psutil.net_io_counters(pernic=False, nowrap=True).packets_sent,
               'net_counter_packets_recv': psutil.net_io_counters(pernic=False, nowrap=True).packets_recv
               }
    return network


def sensor_info():
    sensor = {'sensor_battery': psutil.sensors_battery().percent}
    return sensor
