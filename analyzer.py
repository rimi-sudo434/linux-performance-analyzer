import os
import platform
import socket
import getpass
import shutil
from datetime import datetime

print("=" * 36)
print("     Linux Performance Analyzer")
print("=" * 36)
print()

print(f"OS          : {platform.system()} {platform.release()}")
print(f"Hostname    : {socket.gethostname()}")
print(f"User        : {getpass.getuser()}")

total, used, free = shutil.disk_usage("/")

print(f"Disk Total  : {total // (1024**3)} GB")
print(f"Disk Used   : {used // (1024**3)} GB")
print(f"Disk Free   : {free // (1024**3)} GB")

print(f"Date & Time : {datetime.now().strftime('%d %B %Y %I:%M:%S %p')}")

print()
print("=" * 36)
