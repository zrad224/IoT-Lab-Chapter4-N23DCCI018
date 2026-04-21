import psutil
from datetime import datetime
from time import sleep

# Mở file log
log_file = open('system_log.txt', 'w')

try:
    while True:
        # Đọc CPU
        cpu_list = psutil.cpu_percent(interval=1, percpu=True)
        cpu_avg = sum(cpu_list) / len(cpu_list)

        # Đọc RAM
        ram = psutil.virtual_memory()
        ram_used_mb = ram.used // (1024 ** 2)
        ram_total_mb = ram.total // (1024 ** 2)
        ram_pct = ram.percent

        # Đọc Disk
        disk = psutil.disk_usage('/')
        disk_pct = disk.percent

        # Cảnh báo 3 mức
        if cpu_avg >= 70:
            status = 'CRITICAL'
        elif cpu_avg >= 30:
            status = 'WARNING'
        else:
            status = 'NORMAL'

        # In đúng format + status
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        line = (
             f'[{now}] CPU: {cpu_avg:.1f}% │ '
             f'RAM: {ram_used_mb}/{ram_total_mb} MB ({ram_pct}%) │ '
             f'Disk: {disk_pct}% │ {status}'
        )
        print(line)

        # In dòng cảnh báo riêng nếu không NORMAL
        if status != 'NORMAL':
            print(f'  ⚠ {status}: CPU đang ở {cpu_avg:.1f}%')

        # Ghi log + flush
        log_file.write(line + '\n')
        log_file.flush()

        sleep(2)

except KeyboardInterrupt:
    print('\nDừng giám sát.')

finally:
    log_file.close()
    print('Log saved to system_log.txt')
