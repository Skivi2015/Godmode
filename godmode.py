#!/usr/bin/env python3
"""
Godmode - System Diagnostics Tool
A simple tool to run system diagnostics and provide system information.
"""

import os
import sys
import platform
import shutil
import subprocess
import time
from datetime import datetime


class GodmodeDiagnostics:
    """Main diagnostics class for system monitoring."""
    
    def __init__(self):
        self.start_time = datetime.now()
        
    def display_header(self):
        """Display the application header."""
        print("=" * 60)
        print("🚀 GODMODE - System Diagnostics Tool")
        print("=" * 60)
        print(f"Started at: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
    def get_system_info(self):
        """Get basic system information."""
        print("📊 SYSTEM INFORMATION")
        print("-" * 30)
        print(f"OS: {platform.system()} {platform.release()}")
        print(f"Architecture: {platform.architecture()[0]}")
        print(f"Processor: {platform.processor()}")
        print(f"Hostname: {platform.node()}")
        print(f"Python Version: {platform.python_version()}")
        print(f"Current Working Directory: {os.getcwd()}")
        print(f"User: {os.getenv('USER', 'unknown')}")
        print()
        
    def get_cpu_info(self):
        """Get CPU usage information using system commands."""
        print("🖥️  CPU DIAGNOSTICS")
        print("-" * 30)
        
        # Get CPU count
        try:
            cpu_count = os.cpu_count()
            print(f"CPU Cores: {cpu_count}")
        except:
            print("CPU Cores: Unable to determine")
            
        # Get load average on Unix systems
        if platform.system() != 'Windows':
            try:
                load_avg = os.getloadavg()
                print(f"Load Average (1m, 5m, 15m): {load_avg[0]:.2f}, {load_avg[1]:.2f}, {load_avg[2]:.2f}")
            except:
                print("Load Average: Not available")
        
        # Try to get CPU info from /proc/cpuinfo on Linux
        if platform.system() == 'Linux':
            try:
                with open('/proc/cpuinfo', 'r') as f:
                    lines = f.readlines()
                    for line in lines[:10]:  # Show first 10 lines
                        if line.strip():
                            print(f"  {line.strip()}")
                    if len(lines) > 10:
                        print("  ...")
            except:
                print("  CPU details not available")
        print()
        
    def get_memory_info(self):
        """Get memory usage information."""
        print("💾 MEMORY DIAGNOSTICS")
        print("-" * 30)
        
        # Try to get memory info from /proc/meminfo on Linux
        if platform.system() == 'Linux':
            try:
                with open('/proc/meminfo', 'r') as f:
                    for line in f:
                        if any(keyword in line for keyword in ['MemTotal:', 'MemFree:', 'MemAvailable:', 'SwapTotal:', 'SwapFree:']):
                            print(f"  {line.strip()}")
            except:
                print("  Memory information not available")
        else:
            print("  Memory diagnostics available on Linux systems")
        print()
        
    def get_disk_info(self):
        """Get disk usage information."""
        print("💿 DISK DIAGNOSTICS")
        print("-" * 30)
        
        # Get disk usage for current directory
        try:
            total, used, free = shutil.disk_usage('/')
            print(f"Root filesystem:")
            print(f"  Total: {self.bytes_to_gb(total):.2f} GB")
            print(f"  Used: {self.bytes_to_gb(used):.2f} GB")
            print(f"  Free: {self.bytes_to_gb(free):.2f} GB")
            print(f"  Usage: {(used / total) * 100:.1f}%")
        except:
            print("  Root filesystem info not available")
            
        # Try to get mount info on Unix systems
        if platform.system() != 'Windows':
            try:
                result = subprocess.run(['df', '-h'], capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    print("\nFilesystem usage:")
                    lines = result.stdout.strip().split('\n')
                    for line in lines[:6]:  # Show header + first 5 filesystems
                        print(f"  {line}")
                    if len(lines) > 6:
                        print("  ...")
            except:
                print("  Detailed filesystem info not available")
        print()
                
    def get_network_info(self):
        """Get basic network information."""
        print("🌐 NETWORK DIAGNOSTICS")
        print("-" * 30)
        
        # Try to get network interface info
        if platform.system() != 'Windows':
            try:
                # Check if ifconfig or ip command is available
                if shutil.which('ip'):
                    result = subprocess.run(['ip', 'addr', 'show'], capture_output=True, text=True, timeout=10)
                    if result.returncode == 0:
                        print("Network interfaces (ip addr):")
                        lines = result.stdout.strip().split('\n')
                        for line in lines[:15]:  # Show first 15 lines
                            if line.strip():
                                print(f"  {line}")
                        if len(lines) > 15:
                            print("  ...")
                elif shutil.which('ifconfig'):
                    result = subprocess.run(['ifconfig'], capture_output=True, text=True, timeout=10)
                    if result.returncode == 0:
                        print("Network interfaces (ifconfig):")
                        lines = result.stdout.strip().split('\n')
                        for line in lines[:15]:  # Show first 15 lines
                            if line.strip():
                                print(f"  {line}")
                        if len(lines) > 15:
                            print("  ...")
                else:
                    print("  Network interface tools not available")
            except:
                print("  Network information not available")
        else:
            print("  Network diagnostics available on Unix systems")
        print()
        
    def get_process_info(self):
        """Get running process information."""
        print("⚙️  PROCESS DIAGNOSTICS")
        print("-" * 30)
        
        # Try to get process info using ps command on Unix systems
        if platform.system() != 'Windows':
            try:
                result = subprocess.run(['ps', 'aux'], capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    lines = result.stdout.strip().split('\n')
                    print(f"Total processes found: {len(lines) - 1}")  # Subtract header line
                    print("\nTop processes:")
                    for line in lines[:11]:  # Header + top 10 processes
                        print(f"  {line}")
                    if len(lines) > 11:
                        print("  ...")
            except:
                print("  Process information not available")
        else:
            print("  Process diagnostics available on Unix systems")
        print()
        
    def bytes_to_gb(self, bytes_value):
        """Convert bytes to gigabytes."""
        return bytes_value / (1024 ** 3)
        
    def bytes_to_mb(self, bytes_value):
        """Convert bytes to megabytes."""
        return bytes_value / (1024 ** 2)
        
    def run_diagnostics(self):
        """Run all diagnostic checks."""
        self.display_header()
        self.get_system_info()
        self.get_cpu_info()
        self.get_memory_info()
        self.get_disk_info()
        self.get_network_info()
        self.get_process_info()
        
        end_time = datetime.now()
        duration = end_time - self.start_time
        print("=" * 60)
        print(f"✅ Diagnostics completed in {duration.total_seconds():.2f} seconds")
        print("=" * 60)


def main():
    """Main entry point for the application."""
    try:
        print("🔧 Launching Godmode Diagnostics...")
        time.sleep(1)  # Brief pause for dramatic effect
        
        diagnostics = GodmodeDiagnostics()
        diagnostics.run_diagnostics()
        
        return 0
    except KeyboardInterrupt:
        print("\n\n❌ Diagnostics interrupted by user.")
        return 1
    except Exception as e:
        print(f"\n\n❌ Error running diagnostics: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())