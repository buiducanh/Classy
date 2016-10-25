# Classy

Python application to resolve class schedules

    python schedule_parser.py [INPUT]

Schedule format:

    course [courseName] [integerCredit]
    [Mo/Tu/We/Th/Fr...] [startTime] [endTime]

    Adds whatever number of lines of days for each course as you like.
    The time format must follow the convention "HH:MMam" or "HH:MMpm."
    See `schedule.sc` for an example.
