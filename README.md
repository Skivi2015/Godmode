# Godmode

A powerful system diagnostics tool that provides comprehensive system information and monitoring capabilities.

## Features

🚀 **Easy Launch** - Simple one-command execution  
📊 **System Information** - OS, architecture, hostname, and user details  
🖥️ **CPU Diagnostics** - Core count, load averages, and processor information  
💾 **Memory Diagnostics** - RAM and swap usage statistics  
💿 **Disk Diagnostics** - Filesystem usage and disk space information  
🌐 **Network Diagnostics** - Network interface configuration and status  
⚙️ **Process Diagnostics** - Running process count and top processes  

## Quick Start

### Option 1: Use the launcher script
```bash
./launch.sh
```

### Option 2: Run directly with Python
```bash
python3 godmode.py
```

### Option 3: Make it executable and run
```bash
chmod +x godmode.py
./godmode.py
```

## Requirements

- Python 3.x (uses only built-in libraries)
- Unix-like system (Linux/macOS) for full functionality
- Basic system commands: `ps`, `df`, `ip` or `ifconfig`

## Output

The tool provides detailed diagnostics including:
- System information and configuration
- Real-time CPU usage and load averages
- Memory and swap utilization
- Disk space usage across filesystems
- Network interface configuration
- Running process information

## Example Output

```
============================================================
🚀 GODMODE - System Diagnostics Tool
============================================================
Started at: 2025-08-31 11:57:11

📊 SYSTEM INFORMATION
------------------------------
OS: Linux 6.11.0-1018-azure
Architecture: 64bit
Processor: x86_64
Hostname: example-host
Python Version: 3.12.3
Current Working Directory: /path/to/godmode
User: runner

🖥️  CPU DIAGNOSTICS
------------------------------
CPU Cores: 4
Load Average (1m, 5m, 15m): 0.39, 0.21, 0.11
...

✅ Diagnostics completed in 0.03 seconds
```

## License

Open source - feel free to use and modify as needed.