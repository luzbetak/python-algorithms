import calendar


# https://www.geeksforgeeks.org/calendar-functions-in-python-set-2monthrange-prcal-weekday/?ref=lbp
# https://www.geeksforgeeks.org/python-calendar-module/

def display_month():
    yy = 2022
    mm = 1

    # display the calendar
    print(calendar.month(yy, mm))


def display_range():
    # using monthrange() to print start week day and
    # number of month
    print("The start week number and no. of days of month : ", end="")
    print(calendar.monthrange(2008, 2))


def display_year():
    # using prcal() to print calendar of 1997
    print("The calendar of 1997 is : ")
    calendar.prcal(1997, 2, 1, 6)


if __name__ == "__main__":
    display_range()
    print("-" * 80)
    display_year()
    print("-" * 80)
    display_month()
