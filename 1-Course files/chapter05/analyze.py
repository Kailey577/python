f = open("silly.txt", "r")

line_count = 0
word_count = 0
char_count = 0
for line in f:
    line_count += 1
    words = line.split()
    for word in words:
        word_count += 1
        for char in word:
            char_count += 1
print(f"Lines {line_count}\nWords {word_count}\nChars{char_count}")
