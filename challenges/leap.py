import sys


def year_argument_is_valid():
    """Checks if the argument passed in to the command line is a valid year"""
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        return False

    year = int(sys.argv[1])
    if not isinstance(year, int) or year < 1900 or year > (10 ** 5):
        return False
    return True


def check_if_year_is_leap(year):
    """Checks if the year is a leap year or not"""
    is_leap = False

    if not (year % 4) or (not (year % 100) and not (year % 400)):
        return True
    return False


if __name__ == "__main__":
    if year_argument_is_valid():
        if check_if_year_is_leap(int(sys.argv[1])):
            print("Leap year")
        else:
            print("Not leap year")
    else:
        sys.stderr.write("Invalid year\n")

