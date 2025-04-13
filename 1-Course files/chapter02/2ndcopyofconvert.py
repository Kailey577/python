# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    celsius = 10
    for i in range(10):

        fahrenheit = 9/5 * celsius + 32

        print(str(celsius)+"="+str(fahrenheit))
        celsius = celsius + 10

main()

