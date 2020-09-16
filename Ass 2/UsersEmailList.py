import re
f=open("F:\\uni\RKU\\5th Sem\Python Programming II - CE523\ASS Py Files\data.txt",'r')
result = f.read()
# pattern = re.compile(r"[.A-Za-z0-9-]+@[A-Za-z0-9.-]+[.A-Za-z0-9.-]")
# pattern_name = re.compile(r"M[.A-Za-z0-9-]+\D\S+")
pattern = re.compile(r"[.\w-]+@[\w.-]+[.\w.-]")
file = pattern.finditer(result)
email=[]
for line in file:
    email.append(line)
for i in email:
    print(i.group())
f.close()