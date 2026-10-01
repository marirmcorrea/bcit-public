import dow


def getDayOfTheWeekForUserDate():
    month = int(input("Enter the month (1-12): "))
    day = int(input("Enter the day: "))
    year = int(input("Enter the year: "))

    weekday = dow.getDayOfTheWeek(year, month, day)
    print(f"{month}-{day}-{year} is a {weekday.lower()}.")


if __name__ == "__main__":
    dow.makeCalendar()
    print()
    getDayOfTheWeekForUserDate()