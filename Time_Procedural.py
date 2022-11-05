
def time_check(seconds, minutes, hours, days):
    """
    parameters:
        seconds -> int
        minutes -> int
        hours -> int
        days -> int

    This function checks if:
        1. The seconds input value is an integer and then less than 60 or not a negative value.
        2. The minutes input value is an integer and then less than 60 or not a negative value.
        3. The hours input value is an integer and then less than 24 or not a negative value.

    returns -> bool
        True / False
    """
    if not isinstance(seconds, int):
        raise ValueError('Seconds must be an integer!')
    elif seconds >= 60 or seconds < 0:
        print(
            "Sorry Seconds value cannot be greater than or equal to 60 and cannot be a negative value and must be a string")
        return False
    if not isinstance(minutes, int):
        raise ValueError('Minute must be an integer!')
    elif minutes >= 60 or minutes < 0:
        print(
            "Sorry minutes cannot be greater than  than or equal to 60 and cannot be a negative value and must be a string")
        return False
    if not isinstance(hours, int):
        raise ValueError('Hours must be an integer!')
    elif hours >= 24 or hours < 0:
        print(
            "Sorry hours cannot be greater than  than or equal to 24 and cannot be a negative value and must be a string")
        return False
    if not isinstance(days, int):
        raise ValueError('Sorry days must be an integer')
    return True


def express_time_in_minutes(seconds=0, minutes=0, hours=0, days=0):
    """
    """
    if time_check(seconds, minutes, hours, days):
        total_time_in_minutes = (
            days * 24 * 60) + (hours * 60) + minutes + (seconds // 60)
        return f'The Time in minutes is {total_time_in_minutes} minutes'
    return


def express_time_in_hours(seconds, minutes, hours, days):
    if time_check(seconds, minutes, hours, days):
        total_time_hours = (days * 24) + hours + \
            (minutes // 60) + (seconds // 3600)
        return f'The Time in hours is {total_time_hours} hours'
    return


def time_info(seconds=0, minutes=0, hours=0, days=0):
    if time_check(seconds, minutes, hours, days):
        timeInfo = {'seconds': seconds, 'minutes': minutes,
                    'hours': hours, 'days': days}
        return timeInfo
    return


def addition_of_time(time_info_one, time_info_two):
    seconds_addition = time_info_one['seconds'] + time_info_two['seconds']
    minutes_addition = time_info_one['minutes'] + time_info_two['minutes']
    hours_addition = time_info_one['hours'] + time_info_two['hours']
    days_addition = time_info_one['days'] + time_info_two['days']
    s = 0
    m = 0
    h = 0
    while seconds_addition >= 60:
        # if the seconds additon is greater than 60 or equal you continue to subract 60 from it till its less than 60 and you then save down how many times you did the subraction
        seconds_addition -= 60
        s += 1  # this record how many times 60 is subtracted from seconds_addition
    while minutes_addition >= 60:
        # if the minutes additon is greater than 60 or equal you continue to subract 60 from it till its less than 60 and you then save down how many times you did the subraction
        minutes_addition -= 60
        m += 1  # this record how many times 60 is subtracted from minutes_addition
    while hours_addition >= 24:
        # if the hours additon is greater than 24 or equal you continue to subract 24 from it till its less than 24 and you then save down how many times you did the subraction
        hours_addition -= 24
        h += 1  # this record how many times 24 is subtracted from hours_addition
    total_seconds = seconds_addition
    total_minutes = minutes_addition + s  # adding s to the minutes addition
    total_hours = hours_addition + m  # adding m to the hour addition
    total_days = days_addition + h  # adding h to the days addition
    return f'Total time is {total_days} day(s) {total_hours} hour(s) {total_minutes} minute(s) {total_seconds} second(s)'


def subtraction_of_time(time_info_one, time_info_two):
    if time_info_one['days'] < time_info_two['days']:
        raise ValueError(
            'Sorry second Time canoot be greater than the first one, as time cannot be negative')
    seconds_subtraction = time_info_one['seconds'] - time_info_two['seconds']
    minutes_subtraction = time_info_one['minutes'] - time_info_two['minutes']
    hours_subraction = time_info_one['hours'] - time_info_two['hours']
    days_subtraction = time_info_one['days'] - time_info_two['days']
    s = 0
    m = 0
    h = 0
    while seconds_subtraction < 0:
        # if the seconds subtraction is less than 0(negative) you continue to add 60 to it till its positive and you then save down how many times you did the addition
        seconds_subtraction += 60
        s += 1  # this record how many times 60 is added to seconds_subtraction
    while minutes_subtraction < 0:
        # if the minutes subtraction is less than 0(negative) you continue to add 60 to it till its positive and you then save down how many times you did the addition
        minutes_subtraction += 60
        m += 1  # this record how many times 60 is added to minutes_subtraction
    while hours_subraction < 0:
        # if the hours subtraction is less than 0(negative) you continue to add 24 to it till its positive and you then save down how many times you did the addition
        hours_subraction += 24
        h += 1  # this record how many times 24 is added to minutes_subtraction
    total_seconds = seconds_subtraction
    # subtracting s to the minutes subraction
    total_minutes = minutes_subtraction - s
    total_hours = hours_subraction - m  # subtracting m to the hours subraction
    total_days = days_subtraction - h  # subtracting h to the hours subraction
    return f'Total time is {total_days} day(s) {total_hours} hour(s) {total_minutes} minute(s) {total_seconds} second(s)'


print(express_time_in_minutes(58, 48, 23, 2))
print(express_time_in_hours(58, 48, 23, 2))
time_one = time_info(58, 48, 23, 2)
print(time_one)
time_two = time_info(51, 40, 20, 4)
print(time_two)
print(addition_of_time(time_one, time_two))
print(subtraction_of_time(time_two, time_one))
