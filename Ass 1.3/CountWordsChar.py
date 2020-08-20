fname = input("Enter file name : ")
fh = open(f"F:\\uni\RKU\\5th Sem\Python Programming II - CE523\ASS Py Files\{fname}")
number_of_words = 0
number_of_characters = 0
for line in fh:
    line = line.strip("\n")
    words = line.split()
    number_of_words += len(words)
    number_of_characters += len(line)
fh.close()

print("Total number of words : ",number_of_words)
print("Total number of characters : ",number_of_characters)