#!/usr/bin/env python3
import subprocess
import re
import sys

def get_flir_serial():
    try:
        # Run lsusb -v
        result = subprocess.run(
            ["lsusb", "-v"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        
        output = result.stdout
        # Split into device blocks (separated by empty lines usually, but reliable via "Bus")
        devices = output.split("Bus ")
        
        for device in devices:
            # Check for Point Grey / FLIR vendor
            if "idVendor" in device and ("1e10" in device or "FLIR" in device or "Point Grey" in device):
                # Look for iSerial line
                match = re.search(r"iSerial\s+\d+\s+(\d{7,9})", device)
                if match:
                    print(match.group(1))
                    return 0 # Success
                    
    except Exception as e:
        pass
        
    return 1 # Fail

if __name__ == "__main__":
    sys.exit(get_flir_serial())
