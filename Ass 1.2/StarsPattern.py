def show_star(rows):
    for s in range(0,rows): #s var is for stars pattern.
        print("*"*(s+1),""*(rows-s-1))
show_star(int(input("Enter the number of rows : ")))