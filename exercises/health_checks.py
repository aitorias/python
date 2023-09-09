#!/usr/bin/env python3
import shutil
import psutil


def check_disk_usage(disk):
    disk_usage = shutil.disk_usage(disk)
    free_disk_usage = disk_usage.free / disk_usage.total * 100
    return free_disk_usage > 20


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


print("Error.") if not check_disk_usage(
    "/") or not check_cpu_usage() else print("Everything is OK.")
