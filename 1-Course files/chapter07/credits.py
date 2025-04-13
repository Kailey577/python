
def main():
    credits = int(input("input the amount of credits"))
    if credits<7:
        print("freshman")
    elif credits<16:
        print("Sophomore")
    elif credits<26:
        print("Junior")
    elif credits>= 26:
        print("Senior")
    return

if __name__ == "__main__":
    main()
