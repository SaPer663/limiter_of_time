import ctypes
import os
import subprocess
import time
from get_time import counts_remained_time_till_midnight_in_sec, today
from consts import ip, wireless_url, wireless_headers, mac_address
from requests_to_the_router import mac_filter_on, mac_filter_off, check_mac


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


log = open('log.txt', 'a')
mac_filter_status = False
now_today = today()
count = 0
while True:
    print('START')
    if mac_filter_status:
        mac_filter_status = False
        mac_filter_off()
        print('Dis')
    time_limit = 0
    while True:
        if count % 20 == 0:
            print(f'OK {str(time_limit)}')
        current_day = today()
        log.write(str(current_day) + '\n')
        if current_day != now_today:
            now_today = current_day
            break
        if time_limit == 7200:
            time_limit = 0
            if mac_filter_status == 0:
                mac_filter_status == True
                mac_filter_on()
                log.write('lim = 7200  mac_filter_ON' + '\n')
            time.sleep(counts_remained_time_till_midnight_in_sec() + 32400) # 32400сек- время с 0 до 9
            break
        if check_device(ip): # проверка по ping
            if check_mac(mac_address): #проверка по веб морде роутера
                time_limit += 30
        count += 1        
        time.sleep(30)
    
    mac_filter_off()
    log.write('mac_filter_OFF')







