# Hamid-Mosaku Ahmad
# 190407055
# Systems Engineering

class Time:

    def __init__(self, days: float = 0.0, hours: float = 0.0, minutes: float = 0.0, seconds: float = 0.0):

        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        
    def __str__(self) -> str:

        return f"{float(self._days)} days; {float(self._hours)} hours; {float(self._minutes)} minutes; {float(self._seconds)} seconds"


    def __add__(self, other):

        return self.add(other._days, other._hours, other._minutes, other._seconds)

    def __sub__(self, other):

        return self.subtract(other._days, other._hours, other._minutes, other._seconds)

    def __add__(self, other):
        """
        Add two Time objects
        """
        return self.add(other._days, other._hours, other._minutes, other._seconds)

    def __sub__(self, other):
        """
        Subtract two Time objects
        """
        return self.subtract(other._days, other._hours, other._minutes, other._seconds)
  
    @property
    def days(self):
        """days"""

        return self._days

    @property
    def hours(self):
        """hour (0-23)"""
        return self._hours

    @property
    def minutes(self):
        """minute (0-59)"""
        return self._minutes

    @property
    def seconds(self):
        """seconds (0-59)"""
        return self._seconds

    @property
    def to_days(self):
        """
        Convert time to days
        """
        return self._to_days()

    @property
    def to_hours(self):
        """
        Convert time to hours
        """
        return self._to_hours()

    @property
    def to_minutes(self):
        """
        Convert time to minutes
        """
        return self._to_minutes()

    @property
    def to_seconds(self):
        """
        Convert time to seconds
        """
        return self._to_seconds()


    def days(self):
        """days"""

        return self._days

    def hours(self):
        return self._hours

    def minutes(self):
        return self._minutes

    def seconds(self):
        return self._seconds

    def to_days(self):
        return self._to_days()

    def to_hours(self):
        return self._to_hours()

    def to_minutes(self):
        return self._to_minutes()

    def to_seconds(self):
        return self._to_seconds()

    def _convert_to_day(self, value: int, unit: str):

        if unit == 'days':
            return value
        elif unit == 'hours':
            return value / 24
        elif unit == 'minutes':
            return value / 1440
        elif unit == 'seconds':
            return value / 86400
        else:
            raise ValueError(self.unit_error_message)

    def _convert_to_hours(self, value: int, unit: str):

        if unit == 'days':
            return value * 24
        elif unit == 'hours':
            return value
        elif unit == 'minutes':
            return value / 60
        elif unit == 'seconds':
            return value / 3600
        else:
            raise ValueError(
                "Invalid unit, Valid values are days, hours, minutes, seconds")

    def _convert_to_minutes(self, value: int, unit: str):

        if unit == 'days':
            return value * 1440
        elif unit == 'hours':
            return value * 60
        elif unit == 'minutes':
            return value
        elif unit == 'seconds':
            return value / 60
        else:
            raise ValueError(
                "Invalid unit, Valid values are days, hours, minutes, seconds")

    def _convert_to_seconds(self, value: int, unit: str):

        if unit == 'days':
            return value * 86400
        elif unit == 'hours':
            return value * 3600
        elif unit == 'minutes':
            return value * 60
        elif unit == 'seconds':
            return value
        else:
            raise ValueError(
                "Invalid unit, Valid values are days, hours, minutes, seconds")

    def _to_seconds(self):
        seconds = self._seconds
        minutes = self._convert_to_seconds(self._minutes, "minutes")
        hours = self._convert_to_seconds(self._hours, "hours")
        days = self._convert_to_seconds(self._days, "days")

        return seconds + minutes + hours + days

    def _to_minutes(self):
        minutes = self._minutes
        hours = self._convert_to_minutes(self._hours, "hours")
        days = self._convert_to_minutes(self._days, "days")
        seconds = self._convert_to_minutes(self._seconds, "seconds")

        return minutes + hours + days + seconds

    def _to_hours(self):
        hours = self._hours
        days = self._convert_to_hours(self._days, "days")
        minutes = self._convert_to_hours(self._minutes, "minutes")
        seconds = self._convert_to_hours(self._seconds, "seconds")

        return hours + days + minutes + seconds

    def _to_days(self):

        days = self._days
        hours = self._convert_to_day(self._hours, "hours")
        minutes = self._convert_to_day(self._minutes, "minutes")
        seconds = self._convert_to_day(self._seconds, "seconds")

        days = days + hours + minutes + seconds

        return days

    def subtract(self, days: float = 0.0, hours: float = 0.0, minutes: float = 0.0, seconds: float = 0.0):
        _days = self._days - days
        _hours = self._hours - hours
        _minutes = self._minutes - minutes
        _seconds = self._seconds - seconds

        return Time(_days, _hours, _minutes, _seconds)

    def add(self, days: float = 0.0, hours: float = 0.0, minutes: float = 0.0, seconds: float = 0.0):

        _days = self._days + days
        _hours = self._hours + hours
        _minutes = self._minutes + minutes
        _seconds = self._seconds + seconds

        return Time(_days, _hours, _minutes, _seconds)


getting_time = Time(1, 2, 3, 4)
print(getting_time)
print()
print()


getting_time1 = Time(input("Enter days: "), input("Enter hours: "), input("Enter minutes: "), input("Enter seconds: "))
print(getting_time1)
print()
print()


getting_time2 = Time(input("Enter days: "), input("Enter hours: "), input("Enter minutes: "), input("Enter seconds: "))
print(getting_time2)
print()


print("For converting time to days, hours, minutes, seconds")
t1 = Time(input("Enter days: "), input("Enter hours: "), input("Enter minutes: "), input("Enter seconds: "))
print((t1))
t2 = Time(input("Enter days: "), input("Enter hours: "), input("Enter minutes: "), input("Enter seconds: "))
print()


# classes
print("T1:", str(t1))
print()
print("T2:", str(t2))

# properties
print("T1 Days:", t1.days)
print("T1 hours:", t1.hours)
print("T1 Minutes:", t1.minutes)
print("T1 Seconds:", t1.seconds)
print()

T1 = ((t1))
T2 = ((t2))
# class addition && subtraction
print("Class Addition:", (T1 + T2))

# to other units
print("T1 to days:", t1.to_days)
print("T1 to hours:", t1.to_hours)
print("T1 to minutes:", t1.to_minutes)
print("T1 to seconds:", t1.to_seconds)
print()
