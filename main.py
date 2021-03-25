import influxdb_client
import System
import socket

from getmac import get_mac_address as mac_address
from System import SystemUtil
from datetime import datetime, time

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# hostname = socket.gethostname()
# You can generate a Token from the "Tokens Tab" in the UI
token = "iXs8kq_scyCVtXNGqee34TSD8J7PnCy5Adm6kO57o6_nNEDQZh1vKv34i1fmXebcCJppPP7oZe3xd3xMX0--0w=="
org = "theovady.moutty@edu.itescia.fr"
bucket = "frigreen"

client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=token)


def try_write_cpu_info():
    cpu_info = SystemUtil.cpu_info()
    virtual_cpu_time = cpu_info["cpu_time"]
    virtual_cpu_percent = cpu_info["cpu_percent"]

    sequence = [f"cpu_info,host={mac_address()} cpu_time={virtual_cpu_time}",
                f"cpu_info,host={mac_address()} cpu_percent={virtual_cpu_percent}"]
    return sequence


def try_write_memory_info():
    memory_info = SystemUtil.memory_info()
    virtual_memory_total = memory_info["virtual_memory_total"]
    virtual_memory_available = memory_info["virtual_memory_available"]
    virtual_memory_percent = memory_info["virtual_memory_percent"]

    sequence = [f"memory_info,host={mac_address()} memory_total={virtual_memory_total}",
                f"memory_info,host={mac_address()} memory_available={virtual_memory_available}",
                f"memory_info,host={mac_address()} memory_used_percent={virtual_memory_percent}"]
    return sequence


def try_write_disk_info():
    disk_info = SystemUtil.disk_info()
    disk_memory_total = disk_info["disk_usage_total"]
    disk_memory_used = disk_info["disk_usage_used"]
    disk_memory_used_percent = disk_info["disk_usage_percent"]

    sequence = [f"disk_info,host={mac_address()} disk_memory_total={disk_memory_total}",
                f"disk_info,host={mac_address()} disk_memory_used={disk_memory_used}",
                f"disk_info,host={mac_address()} disk_memory_used_percent={disk_memory_used_percent}"]
    return sequence


def try_write_network_info():
    network_info = SystemUtil.network_info()
    net_counter_bytes_sent = network_info["net_counter_bytes_sent"]
    net_counter_bytes_received = network_info["net_counter_bytes_recv"]

    sequence = [f"network_info,host={mac_address()} net_counter_bytes_sent={net_counter_bytes_sent}",
                f"network_info,host={mac_address()} net_counter_bytes_received={net_counter_bytes_received}"]
    return sequence


def try_write_sensor_info():
    sensor_info = SystemUtil.sensor_info()
    sensor_battery = sensor_info["sensor_battery"]

    sequence = [f"sensor_info,host={mac_address()} sensor_battery={sensor_battery}"]
    return sequence


def try_write():
    write_api = client.write_api(write_options=SYNCHRONOUS)

    launched = False
    while True:
        if datetime.now().second % 5 == 0:
            if not launched:
                write_api.write(bucket, org, try_write_cpu_info())
                write_api.write(bucket, org, try_write_memory_info())
                write_api.write(bucket, org, try_write_disk_info())
                write_api.write(bucket, org, try_write_network_info())
                write_api.write(bucket, org, try_write_sensor_info())
                launched = True
                print("Update")
        else:
            launched = False
    # data = f'mem,host={mac_address()} used_percent={percent}'
    # print(data)
    # write_api.write(bucket, org, data)


if __name__ == '__main__':
    try_write()
