import os
import subprocess

def get_hardware_uuid():
    """
    Queries the device's physical motherboard layout directly.
    Retrieves the unique, immutable hardware UUID.
    """
    if os.name == 'nt':
        # Natively queries Windows Management Instrumentation (WMI) via command line
        cmd = "wmic csproduct get uuid"
        output = subprocess.check_output(cmd, shell=True).decode().split()
        return output[1] if len(output) > 1 else "Unknown_Windows_Device"
    else:
        # Fallback simulation profile for testing environment
        return "SIMULATED_MACBOOK_NEO_HARDWARE_ID_10293"



def verify_session(username, expected_uuid):
    """
    Validates the incoming device fingerprint against our database registry.
    Returns True if it matches, False if it is a hijacked or unauthorized machine.
    """
    # 1. Scrape the active machine's physical hardware identifier
    current_device_id = get_hardware_uuid()
    
    # 2. Check if the active fingerprint matches the expected authorized marker
    if current_device_id == expected_uuid:
        return True
        
    return False
