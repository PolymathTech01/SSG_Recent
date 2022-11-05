class TimeArith:
    def __init__(self, days=None, hours=None, minutes=None, seconds=None):
        self._days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def convert_days_to_hours(self):
        """Convert days to hours"""
        print(self._days * 24, "hours")

    def convert_days_to_minutes(self):
        """Convert days to minutes"""
        print(self._days * 24 * 60, "minutes")

    def convert_days_to_seconds(self):
        """Convert days to seconds"""
        print(self._days * 24 * 60 * 60, "seconds")

    def convert_hours_to_minutes(self):
        """Convert hours to minutes"""
        print(self.hours * 60, "minutes")

    def convert_hours_to_seconds(self):
        """Convert hours to seconds"""
        print(self.hours * 60 * 60, "seconds")

    def convert_minutes_to_seconds(self):
        """Convert minutes to seconds"""
        print(self.minutes * 60, "seconds")

    def convert_seconds_to_minutes(self):
        """Convert seconds to minutes"""
        print(self.seconds / 60, "minutes")

    def convert_seconds_to_hours(self):
        """Convert seconds to hours"""
        print(self.seconds / 60 / 60, "hours")

    def subtract_hours_from_days(self):
        """Subtract hours from days"""
        print(self._days * 24 - self.hours, "hours")

    def subtract_minutes_from_hours(self):
        """Subtract minutes from hours"""
        print(self.hours * 60 - self.minutes, "minutes")

    def subtract_seconds_from_minutes(self):
        """Subtract seconds from minutes"""
        print(self.minutes * 60 - self.seconds, "seconds")


TimeArith(days=7,hours=45).subtract_hours_from_days()
