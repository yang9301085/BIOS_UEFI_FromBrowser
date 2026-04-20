#!/usr/bin/env python3
import struct
import os
import time

# First, let's try using the built-in 'fat' module if available,
# but more likely we can use 'fatfs' from pypi or a simpler approach.
# For simplicity, let's try using 'mtools' if they are available, or
# fall back to using a different approach.

print("Trying to copy files to FAT32 image...")

# Let's check if we can use mcopy
import subprocess

try:
    # First, let's just create a test file with our efi and startup.nsh
    efi_path = "/workspace/edk2/Build/CustomFormBrowserPkg/DEBUG_GCC/IA32/CustomFormBrowserApp.efi"
    startup_path = "/workspace/startup.nsh"
    img_path = "/workspace/uefi_test_debug.img"
    
    print(f"Checking if files exist:")
    print(f"  EFI: {os.path.exists(efi_path)}")
    print(f"  Startup: {os.path.exists(startup_path)}")
    print(f"  Image: {os.path.exists(img_path)}")
    
    # Let's try using mtools if they are available
    try:
        print("\nTrying mcopy...")
        result = subprocess.run(
            ["mcopy", "-i", img_path, efi_path, "::"],
            capture_output=True,
            text=True
        )
        print(f"mcopy efi result: {result.returncode}")
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
            
        result = subprocess.run(
            ["mcopy", "-i", img_path, startup_path, "::"],
            capture_output=True,
            text=True
        )
        print(f"mcopy startup result: {result.returncode}")
        
        # Verify files are there
        print("\nFiles in image:")
        result = subprocess.run(
            ["mdir", "-i", img_path, "::"],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
            
        print("\nDone!")
    except Exception as e:
        print(f"mtools failed: {e}")
        
except Exception as e:
    print(f"Error: {e}")
