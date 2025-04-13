'''def main():
    n = int(input("How many numbers do you have?"))
    sum = 0.0
    for i in range(n):
        x = float(input("Enter a number>> "))
        sum = sum + x
    print("/nThe average of the numbers is", sum /n)

main()'''


'''for i in range(11):
    print(i)'''
'''def main():
    sum = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":
        x = float(input("Enter a number: "))
        sum = sum + x
        count =+ 1
        moredata = input("Do you have more numbers? Say yes or no: ")
    print("The average of the numbers is",sum/count)

main()'''

'''def main():
    sum = 0.0
    count = 0
    user_input = float(input("Enter a number, negative to quit"))
    while user_input >= 0:
        sum = sum + user_input
        count = count + 1
        user_input = float(input("Enter a number, negative to quit"))
    print(sum/count)
main()'''


'''def main():
    sum = 0.0
    count = 0
    xStr = input("enter a number, ENTER to quit ")
    while xStr != "":
        x = float(xStr)
        sum = sum + x
        count = count + 1
        xStr = input("Enter a number, ENTER to quit")
    print(sum/count)
main()'''

'''def main():
    fileName = input("What file are numbers in?")
    infile = open(fileName,'r')
    sum = 0.0
    count = 0
    for line in infile:
        sum = sum + float(line)
        count = count + 1
    print(sum/count)
main()'''


'''def main():
    fileName = input("What file are numbers in?")
    infile = open(fileName, 'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        sum = sum + float(line)
        count = count + 1
        line = infile.readline()
    print(sum/count)
main()'''

def main():
    fileName = input("What file are the numbers in?")
    infile = open(fileName, 'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != '':
        #update sum and count values in line
        for xStr in line.split(","):
            sum = sum + float(xStr)
            count = count + 1
        line = infile.readline()
    print(sum/count)
main()

#NESTED LOOP


