def oyin_time(seconds, minutes, hours, days):
    if (seconds >= 60 or seconds < 0) and not isinstance(seconds, int):
        print(
            "Sorry the value of seconds must be a string cannot be a negative number and cannot be higher than or equal to 60")
        return False
    if (minutes >= 60 or minutes < 0) and not isinstance(minutes, int):
        print(
            "Sorry minutes must be a string cannot be a negative number and cannot be larger than or equal to 60")
        return False
    if (hours >= 24 or hours < 0) and not isinstance(hours, int):
        print(
            "Sorry hours must be a string cannot be a negative number and cannot be larger than or equal to 24")
        return False
    if not isinstance(days, int):
        print('Sorry days must be an integer')
        return False
    return True


def time_in_minutes(seconds=0, minutes=0, hours=0, days=0):
    if oyin_time(seconds, minutes, hours, days):
        total_time_in_minutes = (
            days * 24 * 60) + (hours * 60) + minutes + (seconds // 60)
        return f'The Time in minutes is {total_time_in_minutes} minutes'
    return


def time_in_hours(seconds, minutes, hours, days):
    if oyin_time(seconds, minutes, hours, days):
        total_time_hours = (days * 24) + hours + \
            (minutes // 60) + (seconds // 3600)
        return f'The Time in hours is {total_time_hours} hours'
    return


def time_info(seconds=0, minutes=0, hours=0, days=0):
    if oyin_time(seconds, minutes, hours, days):
        timeInfo = {'seconds': seconds, 'minutes': minutes,
                    'hours': hours, 'days': days}
        return timeInfo
    return


def add_time(time_info_one, time_info_two):
    seconds_addition = time_info_one['seconds'] + time_info_two['seconds']
    minutes_addition = time_info_one['minutes'] + time_info_two['minutes']
    hours_addition = time_info_one['hours'] + time_info_two['hours']
    days_addition = time_info_one['days'] + time_info_two['days']
    s = 0
    m = 0
    h = 0
    while seconds_addition >= 60:
        # If the seconds addition is higher than or equal to 60 you keep deducting 60 from it until it is less than 60 at which point you record how many times you deducted 60
        seconds_addition -= 60
        s += 1  # the number of times 60 is deducted from seconds addition is recorded here
    while minutes_addition >= 60:
        # If the minutes addition is higher than or equal to 60 you keep subtracting 60 until it is less than 60 at which point you record how many times you conducted the subtraction
        minutes_addition -= 60
        m += 1  # This counts the number of times 60 is taken away from minutes addition
    while hours_addition >= 24:
        # If the hours addition is higher than or equal to 24 you keep subtracting 24 until it is less than 24 at which point you record how many times you conducted the subtraction
        hours_addition -= 24
        h += 1  # This counts the number of times 24 is taken away from hours addition
    total_seconds = seconds_addition
    total_minutes = minutes_addition + s  # adding s to the minutes addition
    total_hours = hours_addition + m  # adding m to the hour addition
    total_days = days_addition + h  # adding h to the days addition
    return f'Total time is {total_days} day(s) {total_hours} hour(s) {total_minutes} minute(s) {total_seconds} second(s)'


def subtraction_of_time(time_info_one, time_info_two):
    if time_info_one['days'] < time_info_two['days']:
        raise ValueError(
            'Sorry time cannot be negative it cannot be greater than the first one')
    seconds_subtraction = time_info_one['seconds'] - time_info_two['seconds']
    minutes_subtraction = time_info_one['minutes'] - time_info_two['minutes']
    hours_subraction = time_info_one['hours'] - time_info_two['hours']
    days_subtraction = time_info_one['days'] - time_info_two['days']
    s = 0
    m = 0
    h = 0
    while seconds_subtraction < 0:
        # If the seconds subtraction is less than 0 (negative) add 60 to it repeatedly until it is positive at which point you record how many times you added
        seconds_subtraction += 60
        s += 1  # this record how many times 60 is added to seconds_subtraction
    while minutes_subtraction < 0:
        # If the minutes subtraction is less than 0 (negative), keep adding 60 until it is positive, and then record how many times you added.
        minutes_subtraction += 60
        m += 1  # this record how many times 60 is added to minutes_subtraction
    while hours_subraction < 0:
        # If the hours subtraction is less than 0 (negative), keep adding 24 until it is positive, and then record how many times you added.
        hours_subraction += 24
        h += 1  # this record how many times 24 is added to minutes_subtraction
    total_seconds = seconds_subtraction
    # subtracting s to the minutes subraction
    total_minutes = minutes_subtraction - s
    total_hours = hours_subraction - m  # subtracting m to the hours subraction
    total_days = days_subtraction - h  # subtracting h to the hours subraction
    return f'Total time is {total_days} day(s) {total_hours} hour(s) {total_minutes} minute(s) {total_seconds} second(s)'


print(time_in_minutes(58, 48, 23, 2))
print(time_in_hours(58, 48, 23, 2))
time_one = time_info(58, 48, 23, 2)
print(time_one)
time_two = time_info(51, 40, 20, 4)
print(time_two)
print(add_time(time_one, time_two))
print(subtraction_of_time(time_two, time_one))
