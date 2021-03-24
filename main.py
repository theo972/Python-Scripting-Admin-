import influxdb_client
import System
import socket

from System import SystemUtil
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


hostname = socket.gethostname()
# You can generate a Token from the "Tokens Tab" in the UI
token = "YxNxUR3neGuTvdhcbnMg7Ra3EzSNvyMgmOY69gSRIwNV3YhUQViMYB1GXqzkwVcYNoUTVJF6_4Bpzaa-l68OjA=="
org = "anthony.bac@edu.itescia.fr"
bucket = "anthony.bac's Bucket"

client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=token)


def try_write():
    write_api = client.write_api(write_options=SYNCHRONOUS)

    memory_info = SystemUtil.memory_info()
    virtual_memory = memory_info["virtual_memory"]

    percent = virtual_memory.percent
    print(percent)
    data = f'mem,host="{hostname}" used_percent={percent}'
    print(data)
    write_api.write(bucket, org, data)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    try_write()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
