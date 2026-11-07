"""
Security System - Windows Server Gatekeeper
File: gatekeeper.py
"""

import hashlib
import os 
import secrets
import subprocess

# Secure baseline path for log files
LOG_FILE = "C: \\SecurityLogs\\server_audit.log" if os.name == 'nt' else "server_audit.log"

def log_event(message):
    """Appends security traces directily to our local audit trail."""
    with open(LOG_FILE, "a") as f:
        f.write(f"[LOG]: {message}\n")


def generate_one_time_password(username):
    """
    Generates a secure, temporary password. Displays it ONCE,
    then returns the secure SHA-256 hash to be saved on the server.
    """
    # 1. Create an 8-character secure random token
    raw_password = secrets.token_hex(4) 
    
    # 2. Do not display the plain-text password in logs/console output
    print(f"⚠️  TEMPORARY CREDENTIAL GENERATED FOR [{username}].")
    print("⚠️  Credential value is hidden for security.")
    
    # 3. Hash the password immediately for secure storage
    hashed = hashlib.sha256(raw_password.encode()).hexdigest()
    
    # 4. Write a trace entry to our audit log
    log_event(f"New one-time credential hash created for user: {username}")
    
    # 5. Return only the safe, scrambled hash
    return hashed      


def set_windows_folder_access(username, folder_path, permission_type="R"):
    """
    Natively controls Windows file security!
    Runs the native Windows 'icacls' command via a background process.
    Permissions: 'R' = Read Only, 'F' = Full Control, 'D' = Deny Access
    """
    if os.name != 'nt':
        return f"[Simulation Mode]: Set {permission_type} permissions on {folder_path} for {username}"
        
    try:
        # Command syntax: icacls "C:\SharedFolder" /grant username:(R)
        command = f'icacls "{folder_path}" /grant {username}:({permission_type})'
        
        # Execute the command silently inside the Windows system shell
        subprocess.run(command, shell=True, check=True)
        
        log_event(f"Admin updated NTFS file permissions for {username} on {folder_path}")
        return "NTFS Permissions Updated Successfully."
        
    except subprocess.CalledProcessError as e:
        log_event(f"FAIL: Failed to update NTFS permissions for {username} on {folder_path}")
        return f"Error executing native system command: {e}"
