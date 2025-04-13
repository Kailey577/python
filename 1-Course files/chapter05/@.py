
user_input = input("ENTER A FILE: ")

the_file = open(user_input).read()
#print(the_file)
words = len(the_file.split(" "))
print("There are",words,"words")

characters = [x for x in the_file]
print("There are",len(characters),"characters")

