from datetime import date, datetime, time


# Est-ce que texte proposé est dans un format de date ?
def is_a_date(str):
    date = [item for item in str.split('.')]
    if len(date) == 3:
        if int(date[0]) > 0 and int(date[0]) < 32:
            if int(date[1]) > 0 and int(date[1]) < 13:
                if int(date[2]) > 0:
                    return datetime.strptime(str, '%d.%m.%Y').date()
    else:
        return False


# Est-ce que texte proposé est dans un format de temps ?
def is_a_time(str):
    time = [item for item in str.split(':')]
    if len(time) == 3:
        if int(time[0]) >= 0 and int(time[0]) < 25:
            if int(time[1]) >= 0 and int(time[1]) < 60:
                if int(time[2]) >= 0 and int(time[2]) < 60:
                    return datetime.strptime(str, '%H:%M:%S').time()
    else:
        return False
