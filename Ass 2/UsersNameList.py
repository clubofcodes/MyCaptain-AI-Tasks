import re
f=open("F:\\uni\RKU\\5th Sem\Python Programming II - CE523\ASS Py Files\data.txt",'r')
result = f.read()
pattern = re.compile(r"M[.A-Za-z0-9-]+\D\S+")
file = pattern.finditer(result)
name=[]
for line in file:
    name.append(line)
for i in name:
    print(i)
f.close()