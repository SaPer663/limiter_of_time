from datetime import datetime as dt



def counts_remained_time_till_9am_in_sec(): #выдаёт оставшееся время до 09:00
    now = dt.now()
    time_string_of_ISO_format = now.time().isoformat(timespec='seconds')
    current_time_list_hour_min_sec = [int(i) for i in time_string_of_ISO_format.split(':')]
    the_remained_time_sec = 86400 - (current_time_list_hour_min_sec[0] * 3600 +
    current_time_list_hour_min_sec[1] * 60 + current_time_list_hour_min_sec[2])
    return the_remained_time_sec + 32400 # 32400 время от 00:00 до 9:00

def today(): # возвращает сегоднешнее число
    current_date = dt.today()
    return current_date.day

def current_time():
    now = dt.now()
    return now.hour
