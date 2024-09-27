import psutil
import logging

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Define thresholds in percentage
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80


def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        message = f"ALERT: CPU usage is high: {cpu_usage}%"
        print(message)
    else:
        print(f"CPU usage is normal: {cpu_usage}%")


def check_memory_usage():
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        message = f"ALERT: Memory usage is high: {memory.percent}%"
        print(message)
    else:
        print(f"Memory usage is normal: {memory.percent}%")


def check_disk_usage():
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        message = f"ALERT: Disk space usage is high: {disk.percent}%"
        print(message)
    else:
        print(f"Disk space usage is normal: {disk.percent}%")


def check_running_processes():
    process_count = len(psutil.pids())
    print(f"Running processes count: {process_count}")


def system_health_monitoring():
    print("System health monitoring...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()


if __name__ == "__main__":
    system_health_monitoring()
