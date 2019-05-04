import datetime


def counts_remained_time_till_midnight_in_sec():
    now = datetime.datetime.now()
    time_string_of_ISO_format = now.time().isoformat(timespec='seconds')
    current_time_list_hour_min_sec = [int(i) for i in time_string_of_ISO_format.split(':')]
    current_time_sec = 86400 - (current_time_list_hour_min_sec[0] * 3600 +
    current_time_list_hour_min_sec[1] * 60 + current_time_list_hour_min_sec[2])
    return current_time_sec
    