import os
import sys

def get_uptime():
    # For Linux systems
    if sys.platform.startswith('linux'):
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            return uptime_seconds
    # For macOS systems
    elif sys.platform == 'darwin':
        import subprocess
        output = subprocess.check_output(['sysctl', '-n', 'kern.boottime']).decode()
        import re, time
        m = re.search(r'{ sec = (\d+),', output)
        if m:
            boot_time = int(m.group(1))
            uptime_seconds = time.time() - boot_time
            return uptime_seconds
    else:
        raise NotImplementedError('Unsupported OS')

def print_uptime():
    uptime_seconds = get_uptime()
    uptime_string = f"System Uptime: {uptime_seconds:.2f} seconds"
    print(uptime_string)

if __name__ == "__main__":
    print_uptime()
