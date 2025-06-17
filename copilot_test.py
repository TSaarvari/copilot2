import sys
import subprocess
import time

def get_linux_uptime():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            return uptime_seconds
    except Exception as e:
        print(f"Error reading /proc/uptime: {e}")
        return None

def get_macos_uptime():
    try:
        result = subprocess.run(['sysctl', '-n', 'kern.boottime'],
                               capture_output=True, text=True, check=True)
        import re
        m = re.search(r'{ sec = (\d+),', result.stdout)
        if m:
            boot_time = int(m.group(1))
            uptime_seconds = time.time() - boot_time
            return uptime_seconds
        else:
            print("Could not parse kern.boottime output.")
            return None
    except Exception as e:
        print(f"Error running sysctl: {e}")
        return None

def print_uptime():
    if sys.platform.startswith('linux'):
        uptime = get_linux_uptime()
    elif sys.platform == 'darwin':
        uptime = get_macos_uptime()
    else:
        print("Unsupported operating system.")
        return

    if uptime is not None:
        print(f"System Uptime: {uptime:.2f} seconds")
    else:
        print("Could not determine system uptime.")

if __name__ == "__main__":
    print_uptime()
