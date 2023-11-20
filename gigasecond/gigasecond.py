import datetime

def add(moment):
    new_time = moment + datetime.timedelta(seconds=1e9)
    return datetime.datetime(
        new_time.year,
        new_time.month,
        new_time.day,
        new_time.hour,
        new_time.minute,
        new_time.second)
