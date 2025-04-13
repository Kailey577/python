
def main():
    m = int(input("Enter your first value: "))
    n = int(input("Enter your second value: "))

    while m > 0:
        n, m = m, n%m

    print(n)

main()