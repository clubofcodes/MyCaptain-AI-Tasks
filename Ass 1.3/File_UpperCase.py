fname = input("Enter file name: ")
fh = open(f"F:\\uni\RKU\\5th Sem\Python Programming II - CE523\ASS Py Files\{fname}")    #file handling
#fx & fy scale factor along the horizontal and vertical axis.
for fx in fh: 
    fy = fx.rstrip()
    print(fy.upper())