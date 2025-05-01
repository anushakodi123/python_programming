
from copy import copy
import calendar

def print_time(time):
    s = f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}'
    return s

class Time:
    """Represents a time of day."""

def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time

start = make_time(9, 20, 0)
end = copy(start)
print(print_time(end))


def substract_time(time1, time2):
    time1_seconds = time1.hour * 3600 + time1.minute * 60 + time1.second
    time2_Seconds = time2.hour * 3600 + time2.minute * 60 + time2.second

    if(time1_seconds > time2_Seconds):
        time2_Seconds = time2_Seconds + (24 * 3600)
    seconds_diff = time2_Seconds - time1_seconds
    return seconds_diff


time1 = make_time(10, 30, 0)
time2 = make_time(12, 30, 0)

print(substract_time(time1, time2))


def is_after(t1, t2):
    time1_seconds = time1.hour * 3600 + time1.minute * 60 + time1.second
    time2_seconds = time2.hour * 3600 + time2.minute * 60 + time2.second

    seconds_diff = time1_seconds - time2_seconds

    if(seconds_diff < 0):
        return True
    else:
        return False

time1 = make_time(10, 30, 0)
time2 = make_time(12, 30, 0)
print(is_after(time1, time2))

def print_time(date):
    s = f'{date.year}-{date.month:02d}-{date.day:02d}'
    return s

class Date:
    ...

def make_date(year, month, day):
    date = Date()
    date.year = year
    date.month = month
    date.day = day
    
    return print_time(date)

print(make_date(1933, 6, 22))

def print_time(date):
    s = f'{date.year}-{date.month:02d}-{date.day:02d}'
    return s

def make_date1(year, month, day):
    date = Date()
    date.year = year
    date.month = list(calendar.month_name).index(month)
    date.day = day
    
    return date

print(make_date1(1933, "September", 13))


def is_after(date1, date2):
    date1 = make_date1(date1)
    date2 = make_date1(date2)

    if(date2.year - date1.year > 0):
        return True
    elif(date2.year == date1.year):
        if(date2.month > date1.month):
            return True
        elif(date2.month == date1.month):
            if(date2.day > date1.day):
                return True
    return False
        

date1 = make_date1("September", 17, 1933)
date2 = make_date1("December", 12, 1998)

print(is_after(date1, ))   # ➝ 3

