fname = input("Enter file name: ")
fh = open(fname)    #file handling
#fx & fy scale factor along the horizontal and vertical axis.
for fx in fh: 
    fy = fx.rstrip()
    print(fy.upper())