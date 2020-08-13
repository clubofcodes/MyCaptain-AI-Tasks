import re
class toplvl:
    def __init__(self,path):
        self.path=path
    def read_file(self):
        f=open(self.path,'r')
        result=f.read()
        pattern=re.compile(r'(https?://\S+)')
        data=pattern.findall(result)
        url=[]
        for line in data:
            url.append(line)
        print("List of Top Domain urls")
        TLD=re.compile(r'(https?://\S+.(com|in|edu))')       
        Tldfile=TLD.finditer(result)
        topdom=[]        
        for l in Tldfile:
            topdom.append(l)
        for t in topdom:
            print(t)
        f.close()
if __name__ == "__main__":
    rf =toplvl('data.txt')
    rf.read_file()