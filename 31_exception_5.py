#write a program to accept birthdate include day, month and year from user and display message that your birthday is on given date if user gives invalid date(days,month,year)
class InvalidDateException(Exception):
    pass 

try:
    day = int(input("Enter birth day"))
    month = int(input("Enter month"))
    year = int(input("Enter year"))
    if day<1 or day>31:
        raise InvalidDateException("birth day must be between 1 to 31")
    elif month<1 or month>12:
        raise InvalidDateException("month must be between 1 to 12")
    elif year<=0:
        raise InvalidDateException("year must be above 0")
    else:
        print(f"you birth will be on {day}/{month}/{year}")
except InvalidDateException as error:
    print(f"invalid date {error}")