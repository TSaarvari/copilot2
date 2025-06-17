# copilot_test.py

A simple Python script to print the system uptime.

## Features

- Prints system uptime in seconds.
- Supports Linux and macOS.
- Uses robust exception handling for reliability.
- Uses `subprocess.run()` for subprocess calls (no use of deprecated `os.popen()`).
- Modular code with clear function separation.

## Usage

1. Clone or download this repository.
2. Make sure you have Python 3 installed.
3. Run the script from your terminal:

```bash
python copilot_test.py
```

You should see output like:

```
System Uptime: 12345.67 seconds
```

## Requirements

- Python 3.x

## Supported Platforms

- Linux
- macOS

## Code Structure

- `get_linux_uptime()` — Gets uptime from `/proc/uptime` (Linux).
- `get_macos_uptime()` — Gets uptime using `sysctl` (macOS).
- `print_uptime()` — Prints the system uptime.

## Error Handling

If the script cannot determine the uptime or encounters an error, it will print a user-friendly error message.

## License

This project is provided for educational and demonstration purposes.
