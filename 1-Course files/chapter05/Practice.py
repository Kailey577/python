months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number (1-12:"))
pos = (n-1)*3

MonthAbbrev = months[pos:pos+3]

print(MonthAbbrev)