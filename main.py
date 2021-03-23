# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
import psutil

# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import System
from System import SystemUtil


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

    cpu_info = SystemUtil.cpu_info()
    print(cpu_info)

    memory_info = SystemUtil.memory_info()
    print(memory_info)

    disk_info = SystemUtil.disk_info()
    print(disk_info)

    network_info = SystemUtil.network_info()
    print(network_info)

    sensor_info = SystemUtil.sensor_info()
    print(sensor_info)
