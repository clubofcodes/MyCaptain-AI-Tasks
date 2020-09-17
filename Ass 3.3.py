import numpy as np
row_col = np.genfromtxt("Thums up.csv",delimiter=';',skip_header=1)
quality=row_col[:,11]
lst=[]
# print(quality)
for i in quality:
    if i > 5:
        lst.append(i)
write=np.savetxt('good_thumsup.csv',lst,delimiter=',')
read=open('good_thumsup.csv','r')
print("Data Having Quality above 5 :")
print(read.read())