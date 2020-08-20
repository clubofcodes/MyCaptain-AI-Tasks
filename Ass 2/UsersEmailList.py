import re
f=open("F:\\uni\RKU\\5th Sem\Python Programming II - CE523\ASS Py Files\data.txt",'r')
result = f.read()
pattern = re.compile(r"[.A-Za-z0-9-]+@[A-Za-z0-9.-]+[.A-Za-za-z)-9.-]")
file = pattern.finditer(result)
email=[]
for line in file:
    email.append(line)
for i in email:
    print(i)
f.close()