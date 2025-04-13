speed_limit = int(input("WHAT'S THE SPEED LIMIT???(MILES)"))

ur_speed = int(input("what was ur speed?(MILES)"))

if ur_speed < speed_limit:
    print("your speed was legal")
    quit()

ticket = 50 + 5*(ur_speed - speed_limit)

print("the fine is",ticket)
