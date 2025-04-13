#print("1,2,3,4,5".split(","))

'''coords = input("Enter the point coordinates (x,y:) ").split(",")
print(coords)
print(coords[0])
x,y = (float(coords[0]), float(coords[1]))'''

'''def main():
    print("this program coverts a sequence of Unicode numbers into")
    print("the string of text that it represents./n")

    inString = input("Please enter the Unicode-encoded message:")
    message = ""
    for numStr in inString.split():
        codeNum = int(numStr)
        message = message + chr(codeNum)

    print("/nThe decoded message is:",message)

main()'''

'''s = ("hello, I came here for an argument")
print(s)
print(s.capitalize())

s = ("Hello, I Came hHere For An Argument")
print(s.lower())

s = ("hello, i came here for an argument")
print(s.upper())

s = ("HELLO< I CAME HERE FOR AN ARGUMENT")
print(s.replace("I","you"))'''


'''dateStr = input("Enter a date (mm/dd/yyyy):")

monthStr, dayStr, yearStr = dateStr.split("/")

months = ["january","february","march", "april", "may", "june", "july","august," "september","october", "november","december"]
monthStr = months[int(monthStr)-1]

print("the converted date is:",monthStr,dayStr+",",yearStr)'''


'''print("Hello {0}{1}, you may have won ${2}".format("Mr.","Smith", 1000))
print("This int, {0:5}, was placed in a field of width 5".format(7))
print("This int, {0:10}, was placed in a field of width 10".format(7))
print("This float, {0:10.5}, has width 10 and precision 5".format(3.1415926))
print("This float, {0:10.5f}, is fixed at 5 decimal places".format(3.1415926))
print("This float, {0:0.5},has width 0 and precision 5".format(3.1415926))
print("Compare {0} and {0:0.20}".format(3.14))

#print("right justification: {0:>5}".format("Hi!"))
print("centered: {0:-5}".format("Hi!"))'''

'''def main():
    print("Change Counter/n")
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels"))
    pennies = int(input("Pennies"))

    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies

    print("The total value of your change is ${0}.{1:0>2}".format(total//100,total%100))
main()'''

'''def main():
    print("This program creates a file of usernames from a")
    print("file of names.")

    infileName = input("What file are the names in?")
    outfileName = input("what file should the usernames go in?")

    infile = open(infileName, "r")
    outfile = open(outfileName, "w")
    for line in infile:
        first, last = line.split()
        uname = (first[0]+last[:7].lower())
    print(uname, file = outfile)
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)
main()'''


