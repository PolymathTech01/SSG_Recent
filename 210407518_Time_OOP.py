class TimeArithmetic:
    def __init__(self, seconds=0, minutes=0, hours=0, days=0):
        """
        parameters:
        seconds -> int
        minutes -> int
        hours -> int
        days -> int

        This method checks if:
            1. The seconds input value is an integer and then less than 60 or not a negative value.
            2. The minutes input value is an integer and then less than 60 or not a negative value.
            3. The hours input value is an integer and then less than 24 o
        """
        if not isinstance(seconds, int):
            raise ValueError('Seconds must be an integer!')
        elif seconds >= 60 or seconds < 0:
            raise ValueError(
                "Sorry Seconds value cannot be greater than or equal to 60 and cannot be a negative value")
        if not isinstance(minutes, int):
            raise ValueError('Minute must be an integer!')
        elif minutes >= 60 or minutes < 0:
            raise ValueError(
                "Sorry minutes cannot be greater than  than or equal to 60 and cannot be a negative value")
        if not isinstance(hours, int):
            raise ValueError('Hours must be an integer!')
        if hours >= 24 or hours < 0:
            raise ValueError(
                "Sorry hours cannot be greater than  than or equal to 24 and cannot be a negative value")
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
        self.days = days

    def __call__(self) -> str:

        return f'Time is {self.days} day(s) {self.hours} hours(s) {self.minutes} minutes(s) and {self.seconds} second(s)'

    def express_time_in_minutes(self):
        """
        parameters:
           None

        This method convert time in days, hours and seconds to minutes and add them together

        returns -> str: 
            Time in minutes
        """
        total_time_in_minutes = (
            self.days * 24 * 60) + (self.hours * 60) + self.minutes + (self.seconds // 60)

        return f'The Time in minutes is {total_time_in_minutes} minutes'

    def express_time_in_hours(self):
        """
        parameters:
           None
        This method convert time in days, minutes and seconds to hours and add them together

        returns -> str: 
            Time in hours

        """
        total_time_hours = (self.days * 24) + self.hours + \
            (self.minutes // 60) + (self.seconds // 3600)
        return f'The Time in hours is {total_time_hours} hours'

    def __add__(self, secondTimeInstance):
        """
        parameter: 
            secondTimeInstance -- second TimeArithmetic instance to be added

        This methods add a TimeArithmetic instance to another TimeArithmetic instance 

        returns -> str
            Time in days, hours, minutes and seconds
        """
        seconds_addition = self.seconds + secondTimeInstance.seconds
        minutes_addition = self.minutes + secondTimeInstance.minutes
        hours_addition = self.hours + secondTimeInstance.hours
        days_addition = self.days + secondTimeInstance.days
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

    def __sub__(self, secondTimeInstance):
        """
        parameter: 
            secondTimeInstance -- second TimeArithmetic instance to be subtracted

        This methods subtract a TimeArithmetic instance from another TimeArithmetic instance 

        returns -> str
            Time in days, hours, minutes and seconds
        """
        if self.days < secondTimeInstance.days:
            raise ValueError(
                'Sorry second Time instance canoot be greater than the first one, as time cannot be negative')
        seconds_subtraction = self.seconds - secondTimeInstance.seconds
        minutes_subtraction = self.minutes - secondTimeInstance.minutes
        hours_subraction = self.hours - secondTimeInstance.hours
        days_subtraction = self.days - secondTimeInstance.days
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


time_one = TimeArithmetic(58, 48, 23, 2)
time_two = TimeArithmetic(51, 40, 20, 4)

print(time_one.express_time_in_minutes())

print(time_one.express_time_in_hours())

print(time_two.express_time_in_minutes())

print(time_two.express_time_in_hours())

addition_of_time = time_one + time_two
print('Additon of time: ', addition_of_time)

subtraction_of_time = time_two - time_one
print('Subraction of Time: ', subtraction_of_time)


print(type(time_one))