import sched

import influxdb_client
import System
import socket

from getmac import get_mac_address as mac_address
from System import SystemUtil
from apscheduler.schedulers.blocking import BlockingScheduler

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# hostname = socket.gethostname()
# You can generate a Token from the "Tokens Tab" in the UI
token = "iXs8kq_scyCVtXNGqee34TSD8J7PnCy5Adm6kO57o6_nNEDQZh1vKv34i1fmXebcCJppPP7oZe3xd3xMX0--0w=="
org = "theovady.moutty@edu.itescia.fr"
bucket = "frigreen"

client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)


def try_write_cpu_info():
    """
        get every info from processor and returns it as a sequence
    :return:
    """
    cpu_info = SystemUtil.cpu_info()
    virtual_cpu_time = cpu_info["cpu_time"]
    virtual_cpu_percent = cpu_info["cpu_percent"]

    sequence = [f"cpu_info,host={mac_address()} cpu_time={virtual_cpu_time}",
                f"cpu_info,host={mac_address()} cpu_percent={virtual_cpu_percent}"]
    return sequence


def try_write_memory_info():
    """
        get every info from ram and returns it as a sequence
    :return:
    """
    memory_info = SystemUtil.memory_info()
    virtual_memory_total = memory_info["virtual_memory_total"]
    virtual_memory_available = memory_info["virtual_memory_available"]
    virtual_memory_percent = memory_info["virtual_memory_percent"]

    sequence = [f"memory_info,host={mac_address()} memory_total={virtual_memory_total}",
                f"memory_info,host={mac_address()} memory_available={virtual_memory_available}",
                f"memory_info,host={mac_address()} memory_used_percent={virtual_memory_percent}"]
    return sequence


def try_write_disk_info():
    """
        get every info from disk and returns it as a sequence
    :return:
    """
    disk_info = SystemUtil.disk_info()
    disk_memory_total = disk_info["disk_usage_total"]
    disk_memory_used = disk_info["disk_usage_used"]
    disk_memory_used_percent = disk_info["disk_usage_percent"]

    sequence = [f"disk_info,host={mac_address()} disk_memory_total={disk_memory_total}",
                f"disk_info,host={mac_address()} disk_memory_used={disk_memory_used}",
                f"disk_info,host={mac_address()} disk_memory_used_percent={disk_memory_used_percent}"]
    return sequence


def try_write_network_info():
    """
        get every info from network and returns it as a sequence
    :return:
    """
    network_info = SystemUtil.network_info()
    net_counter_bytes_sent = network_info["net_counter_bytes_sent"]
    net_counter_bytes_received = network_info["net_counter_bytes_recv"]

    sequence = [f"network_info,host={mac_address()} net_counter_bytes_sent={net_counter_bytes_sent}",
                f"network_info,host={mac_address()} net_counter_bytes_received={net_counter_bytes_received}"]
    return sequence


def try_write_sensor_info():
    """
        get every info from sensor and returns it as a sequence
    :return:
    """
    sensor_info = SystemUtil.sensor_info()
    sensor_battery = sensor_info["sensor_battery"]

    sequence = [f"sensor_info,host={mac_address()} sensor_battery={sensor_battery}"]
    return sequence


def try_write():
    """
    update every sequences on database
    :return:
    """
    write_api.write(bucket, org, try_write_cpu_info())
    write_api.write(bucket, org, try_write_memory_info())
    write_api.write(bucket, org, try_write_disk_info())
    write_api.write(bucket, org, try_write_network_info())
    write_api.write(bucket, org, try_write_sensor_info())
    print("Update")


def interval_try_write():
    """
    Prepare a scheduler with interval for every try_write()
    :return:
    """
    test_scheduler = BlockingScheduler()
    test_scheduler.add_job(try_write, 'interval', seconds=5)
    try:
        test_scheduler.start()
    except (KeyboardInterrupt, SystemError):
        pass


if __name__ == '__main__':
    interval_try_write()
