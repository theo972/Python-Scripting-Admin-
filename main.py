# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
import psutil


# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def cpu_time():
    cpu = psutil.cpu_times()
    print(cpu)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    print(cpu_time())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
