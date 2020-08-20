import re
f=open("F:\\uni\RKU\\5th Sem\Python Programming II - CE523\ASS Py Files\data.txt",'r')
result = f.read()
pattern = re.compile(r"https?://+[-\w.]+[A-Za-z0-9]")
file = pattern.finditer(result)
url=[]
for line in file:
    url.append(line)
for i in url:
    print(i)
f.close()