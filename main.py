import influxdb_client
import System
import socket

from getmac import get_mac_address as mac_address
from System import SystemUtil
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# hostname = socket.gethostname()
# You can generate a Token from the "Tokens Tab" in the UI
token = "YxNxUR3neGuTvdhcbnMg7Ra3EzSNvyMgmOY69gSRIwNV3YhUQViMYB1GXqzkwVcYNoUTVJF6_4Bpzaa-l68OjA=="
org = "anthony.bac@edu.itescia.fr"
bucket = "dear_god"

client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=token)


def try_write_cpu_info():
    """
       Retrieves information from the cpu in the form of a dictionary and sends them in the form of a sequence
       :return: sequence
    """
    cpu_info = SystemUtil.cpu_info()
    virtual_cpu_time = cpu_info["cpu_time"]
    virtual_cpu_percent = cpu_info["cpu_percent"]

    sequence = [f"cpu_info,host={mac_address()} cpu_time={virtual_cpu_time}",
                f"cpu_info,host={mac_address()} cpu_percent={virtual_cpu_percent}"]
    return sequence


def try_write_memory_info():
    """
       Retrieves information from the memory in the form of a dictionary and sends them in the form of a sequence
       :return: sequence
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
       Retrieves information from the disk in the form of a dictionary and sends them in the form of a sequence
       :return: sequence
    """
    memory_info = SystemUtil.disk_info()
    disk_memory_total = memory_info["disk_usage_total"]
    disk_memory_used = memory_info["disk_usage_used"]
    disk_memory_used_percent = memory_info["disk_usage_percent"]

    sequence = [f"disk_info,host={mac_address()} disk_memory_total={disk_memory_total}",
                f"disk_info,host={mac_address()} disk_memory_used={disk_memory_used}",
                f"disk_info,host={mac_address()} disk_memory_used_percent={disk_memory_used_percent}"]
    return sequence


def try_write_network_info():
    """
       Retrieves information from the network in the form of a dictionary and sends them in the form of a sequence
       :return: sequence
    """
    network_info = SystemUtil.network_info()
    net_counter_bytes_sent = network_info["net_counter_bytes_sent"]
    net_counter_bytes_received = network_info["net_counter_bytes_recv"]

    sequence = [f"network_info,host={mac_address()} net_counter_bytes_sent={net_counter_bytes_sent}",
                f"network_info,host={mac_address()} net_counter_bytes_received={net_counter_bytes_received}"]
    return sequence


def try_write_sensor_info():
    """
       Retrieves information from the sensor in the form of a dictionary and sends them in the form of a sequence
      :return: sequence
    """
    sensor_info = SystemUtil.sensor_info()
    sensor_battery = sensor_info["sensor_battery"]

    sequence = [f"sensor_info,host={mac_address()} sensor_battery={sensor_battery}"]
    return sequence


def try_write():
    """ Retrieve the sequences and send them to the database """
    write_api = client.write_api(write_options=SYNCHRONOUS)

    write_api.write(bucket, org, try_write_cpu_info())
    write_api.write(bucket, org, try_write_memory_info())
    write_api.write(bucket, org, try_write_disk_info())
    write_api.write(bucket, org, try_write_network_info())
    write_api.write(bucket, org, try_write_sensor_info())

    # data = f'mem,host={mac_address()} used_percent={percent}'
    # print(data)
    # write_api.write(bucket, org, data)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    try_write()


if __name__ == '__main__':
    print_hi('PyCharm')


