
def is_valid_month(month:int) -> bool:
    # produces true if month is in valid range [1,12]
    return month <= 12 and month >= 1

assert not is_valid_month(-3)

def is_valid_day(month, day, year) -> bool:
    # determines if the given day is consistent with that year
    # takes into account leap years
    if month in [1,3, 5, 7, 8, 10, 12]:
        return 1<= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1<= day <= 30
    elif month == 2:
        if year%4 == 0 and (year % 100 != 0 or year % 400 == 0 ):
            return 1<= day <= 29
        else:
            return 1 <= day <= 28
    return False
#assert is_valid_day(3,29,1995)

#assert is_valid_day(2, 29, 2000)
#assert not is_valid_day(2, 29, 2001)
def main():
    month, day, year = input("ENTER MONTH/DAY/YEAR").split("/")
    month = int(month)
    day = int(day)
    year = int(day)
    if is_valid_day(month,day,year) and is_valid_month(month):
        print("VALID")
    else:
        print("INVALID")

main()



