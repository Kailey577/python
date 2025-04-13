file_object = open("./silly.txt")

all_lines = file_object.read()
name_count = 0
name = "JULIET"
for word in all_lines.strip().split():
    if word.replace(".", "") == name:
        name_count += 1
print(name, "has", name_count, "lines")