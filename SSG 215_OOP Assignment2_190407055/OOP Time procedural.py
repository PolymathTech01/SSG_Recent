# Hamid-Mosaku Ahmad
# 190407055
# Systems Engineering


import typing

# implement time class procedurally


def time(days: float = 0.0, hours: float = 0.0, minutes: float = 0.0, seconds: float = 0.0) -> typing.Dict[str, float]:
    """
    Time

    Can convert supplied time to seconds, minutes, hours, days.
    """
    validate_fields({"days": days, "hours": hours,
                    "minutes": minutes, "seconds": seconds})
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }


def validate_fields(time: typing.Dict[str, float]) -> None:
    """
    Validate fields
    """
    hour = time["hours"]
    minute = time["minutes"]
    second = time["seconds"]

    if not 0 <= hour <= 23:
        raise ValueError('hour must be in 0..23', hour)
    if not 0 <= minute <= 59:
        raise ValueError('minute must be in 0..59', minute)
    if not 0 <= second <= 59:
        raise ValueError('second must be in 0..59', second)


def add(time1: typing.Dict[str, float], time2: typing.Dict[str, float]) -> typing.Dict[str, float]:
    """
    Add two Time objects
    """
    return {
        "days": time1["days"] + time2["days"],
        "hours": time1["hours"] + time2["hours"],
        "minutes": time1["minutes"] + time2["minutes"],
        "seconds": time1["seconds"] + time2["seconds"]
    }


def subtract(time1: typing.Dict[str, float], time2: typing.Dict[str, float]) -> typing.Dict[str, float]:
    """
    Subtract two Time objects
    """
    return {
        "days": time1["days"] - time2["days"],
        "hours": time1["hours"] - time2["hours"],
        "minutes": time1["minutes"] - time2["minutes"],
        "seconds": time1["seconds"] - time2["seconds"]
    }


def convert_to_seconds(time: typing.Dict[str, float]) -> float:
    """
    Convert time to seconds
    """
    return time["days"] * 24 * 60 * 60 + time["hours"] * 60 * 60 + time["minutes"] * 60 + time["seconds"]


def convert_to_minutes(time: typing.Dict[str, float]) -> float:
    """
    Convert time to minutes
    """
    return convert_to_seconds(time) / 60


def convert_to_hours(time: typing.Dict[str, float]) -> float:
    """
    Convert time to hours
    """
    return convert_to_minutes(time) / 60


def convert_to_days(time: typing.Dict[str, float]) -> float:
    """
    Convert time to days
    """
    return convert_to_hours(time) / 24


def main():
    """
    Main function
    """
    time1 = time(5, 21, 53, 34)
    time2 = time(10, 16, 17, 48)

    print(time2)

    print(add(time1, time2))
    print(subtract(time1, time2))


if __name__ == "__main__":
    main()
