from datetime import datetime, time


def is_a_boolean(str):
    if str == 'True':
        return True
    if str == 'False':
        return False
    raise ValueError("huh?")


def is_a_date(str):
    date = [int(item) for item in str.split('.')]
    for part in date:
        part = int(part)
    if date[0] > 0 and date[0] < 32:
        if date[1] > 0 and date[1] < 13:
            if date[2] > 0:
                return datetime.strptime(str, '%d.%m.%y')
    else:
        return False


def is_a_time(str):
    time = [int(item) for item in str.split(':')]
    for part in time:
        part = int(part)
    if time[0] > 0 and time[0] < 25:
        if time[1] > 0 and time[1] < 60:
            if time[2] > 0 and time[2] < 60:
                return datetime.time(hour=time[0],
                                     minute=time[1],
                                     second=time[2])
    else:
        return False


def autoconvert(str):
    for type in (is_a_boolean, int, float, is_a_time, is_a_date):
        try:
            return type(str)
        except ValueError:
            pass
    return str