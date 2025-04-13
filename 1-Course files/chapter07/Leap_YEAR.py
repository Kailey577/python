
def is_century(year: str) -> bool:
    #true if year ends in 000 e.g 2000 3000 1900
    return year[-2::1] == "00"

assert is_century("2000")
assert not is_century("2021")

def is_leap_year(year:str):
    int_year = int(year)
    if is_century(year):
        if int_year % 400 == 0:
            return True
        else:
            return False
    # not century year
    return int_year%4 == 0

assert is_leap_year("2000")

def main():
    user_input = input("Enter the year: ")
    print("it is a leap year true or false:", is_leap_year(user_input))

main()