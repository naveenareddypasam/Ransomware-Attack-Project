import psutil
import time
import shutil
import os

# Specify the backup directory
WATCHED_DIRECTORY = "/home/naveena/Businessfiles"
BACKUP_DIRECTORY = "/home/naveena/Backupfiles"

def backup_files():
    """Backup files before any encryption activity."""
    if not os.path.exists(BACKUP_DIRECTORY):
        os.makedirs(BACKUP_DIRECTORY)
    
    for root, dirs, files in os.walk(WATCHED_DIRECTORY):
        for file in files:
            file_path = os.path.join(root, file)
            backup_path = os.path.join(BACKUP_DIRECTORY, os.path.relpath(file_path, WATCHED_DIRECTORY))
            backup_dir = os.path.dirname(backup_path)
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            shutil.copy2(file_path, backup_path)
            print(f"Backup created for file: {file_path}")

def terminate_suspicious_process(exe_name="securitypatch"):
    """Terminate the specified process if it is found running."""
    for process in psutil.process_iter(['pid', 'name']):
        if exe_name in process.info['name']:
            print(f"Terminating process: {process.info['name']} (PID: {process.info['pid']})")
            process.terminate()

# Backup files first
print("Creating backups before monitoring for ransomware activity...")
backup_files()

# Continuously monitor and terminate process if it appears
print("Monitoring for suspicious process...")
while True:
    terminate_suspicious_process()
    time.sleep(0.01)  # Check every 2 seconds

