name = input("ENTER YOUR NAME: ").lower().strip(" ").replace(" ","")
length = len(name)
the_list = []
the_list[:] = name
print(the_list)
#the_alphabet = ["abcdefghijklmnopqrstuvwxyz"]

total = 0
for character in the_list:
    total = ord(character)+total-96
    print(character)
    print(total)



print(total)