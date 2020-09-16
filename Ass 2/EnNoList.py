import re
f = open("F:\\uni\RKU\\5th Sem\Python Programming II - CE523\ASS Py Files\data.txt","r")
result = f.read()
pattern = re.compile(r'\d{2}\D{5}\d{5}')
file = pattern.finditer(result)
e_no = []
for line in file:
    e_no.append(line)
for i in e_no:
    print(i.group())
f.close()