MONTH_CODES = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
CENTURY_OFFSETS = [6, 4, 2, 0]
WEEKDAYS = [
    "Saturday", "Sunday", "Monday", "Tuesday",
    "Wednesday", "Thursday", "Friday"
]


def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def getDayOfTheWeek(year, month, day):
    # Steps 1–3: calculate using the last two digits.
    last_two_digits = year % 100
    twelves = last_two_digits // 12
    remainder = last_two_digits % 12
    fours = remainder // 4

    # Step 5: find the month code.
    month_code = MONTH_CODES[month - 1]

    # Adjust January and February in leap years.
    if isLeapYear(year) and month in (1, 2):
        month_code -= 1

    # Apply the century offset, which repeats every 400 years.
    century = year // 100
    month_code += CENTURY_OFFSETS[century % 4]

    # Steps 4 and 6: add everything and find the weekday.
    total = twelves + remainder + fours + day + month_code
    return WEEKDAYS[total % 7]


def makeCalendar():
    year = 2026
    days_in_month = [
        31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ]

    if isLeapYear(year):
        days_in_month[1] = 29

    for month in range(1, len(days_in_month) + 1):
        number_of_days = days_in_month[month - 1]

        for day in range(1, number_of_days + 1):
            weekday = getDayOfTheWeek(year, month, day)
            print(f"{month}-{day}-{year} is a {weekday.lower()}.")