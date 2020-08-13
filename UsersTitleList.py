import re
f=open("data.txt",'r')
result = f.read()
pattern = re.compile(r")
file = pattern.finditer(result)
email=[]
for line in file:
    email.append(line)
for i in email:
    print(i)
f.close()