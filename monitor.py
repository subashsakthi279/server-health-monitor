import psutil
import datetime

# --- CONFIGURATION ---
# Set the threshold percentage for alerts
CPU_THRESHOLD = 80.0
MEM_THRESHOLD = 80.0
LOG_FILE = "system_alerts.log"

def check_system_health():
    print("Starting System Health Monitor...")
    
    # 1. Gather System Metrics
    # Get CPU usage over a 1-second interval
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # Get RAM (Memory) usage
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    
    # Print current status to the console
    print(f"Current CPU Usage: {cpu_usage}%")
    print(f"Current Memory Usage: {memory_usage}%")
    
    # 2. Evaluate and Alert
    # Check if either metric exceeds our defined 80% threshold
    if cpu_usage > CPU_THRESHOLD or memory_usage > MEM_THRESHOLD:
        alert_message = f"[{datetime.datetime.now()}] ALERT: High resource usage detected! CPU: {cpu_usage}%, Memory: {memory_usage}%\n"
        
        # Print alert to screen
        print(f"⚠️ {alert_message}")
        
        # Write alert to our log file (the 'a' means append to the end of the file)
        with open(LOG_FILE, "a") as file:
            file.write(alert_message)
            print(f"Alert successfully logged to {LOG_FILE}")
    else:
        print("✅ System resources are within normal limits. No alerts triggered.")

# This ensures the script runs when we execute the file directly
if __name__ == "__main__":
    check_system_health()