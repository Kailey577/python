year = int(input("ENTER YOUR YEAR: "))
if year < 1982 or year > 2048:
    print("NOT VALID")
    quit()

a = year % 18
b = year/4
c = year/7
d = (year + 24)/30
e = (2*b + 4*c + 6*d + 5)/7
print(e)
print(d)
final = d + e
if final > 9:
    print("Easter will be on April",final-9)
if final < 9:
    print("Easter will be on March",22 + final)
