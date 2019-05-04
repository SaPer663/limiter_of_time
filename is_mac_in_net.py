import ctypes
import os
import subprocess
import time
from get_time import counts_remained_time_till_midnight_in_sec


ip = '192.168.0.4'
ip_nat = '192.168.0.8'

encoding = os.device_encoding(1) or ctypes.windll.kernel32.GetOEMCP()

def check_device(ip):
#функция выполняет проверку по ip и mac нахождения телефона в дом. сети и возвр. True or False    
    try:
        subprocess.check_output(rf'ping -n 1 {ip}', encoding=encoding)
        text_arp = subprocess.check_output(rf'arp -a {ip}', encoding=encoding).split()
    except Exception:
        return False
    else:
        if len(text_arp) > 8:
            return True
    return False
time_limit = 7170
while True:
    if time_limit == 7200:
        time_limit = 0
        time.sleep(counts_remained_time_till_midnight_in_sec())
        print('TIME OVER!!!')
        continue
    if check_device(ip):
        time_limit += 30
    time.sleep(30)






