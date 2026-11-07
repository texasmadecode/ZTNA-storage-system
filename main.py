"""
Main Control Room - Security System Simulation Engine
File: main.py
"""
from security_system import gatekeeper
from security_system import fingerprint

def run_security_suite():
    print("=== 🛠️  ADMIN CONFIGURATION SEQUENCE ===")
    
    # 1. Register a user and generate a secure, one-time setup code
    # This prints the raw string once and saves only the secure SHA-256 hash
    password_to_show, user_hash = gatekeeper.generate_one_time_password("employee_01")

    print(f"⚠️  TEMPORARY CREDENTIAL GENERATED FOR [employee_01]: {password_to_show}")
    print("⚠️  Provide this to the user immediately! It is hidden from backend server logs.")

    # 2. Map strict Windows folder permissions natively using our background subprocess tool
    # Runs the native Windows 'icacls' command or falls back gracefully on non-Windows hosts
    folder_status = gatekeeper.set_windows_folder_access(
        username="employee_01", 
        folder_path="C:\\CompanyData\\Accounting", 
        permission_type="R"  # R stands for Read-Only access
    )
    print(f"System Status: {folder_status}\n")


    print("=== 🔐 ZERO-TRUST CONNECTIVITY HANDSHAKE ===")
    
    # This represents the secure baseline hardware profile saved in the server's directory registry
    approved_device_registry = "SIMULATED_MACBOOK_NEO_HARDWARE_ID_10293"

    # 3. Verify physical device integrity before ever prompting the user for a login password
    # Scrapes the local machine's physical layout using deep system calls
    is_hardware_trusted = fingerprint.verify_session("employee_01", approved_device_registry)

    if is_hardware_trusted:
        print("✅ HANDSHAKE PASSED: Active device hardware fingerprint matches our secure registry.")
        gatekeeper.log_event("User employee_01 successfully passed physical device validation.")
        # (This is where your secure gateway protocol would safely prompt them for their password next!)
    else:
        print("🚨 ACCESS BLOCKED: Intruding connection profile detected! Device fingerprint mismatch.")
        gatekeeper.log_event("CRITICAL ALERT: Unauthorized hardware configuration blocked from accessing server gateway.")

if __name__ == "__main__":
    run_security_suite()
