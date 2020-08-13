def showNumbers(limit):
    print("List of Odd & Even Numbers till index :",limit-1)
    for n in range(0,limit):
        if n%2==0:
            print(n,"EVEN")
        else:
            print(n,"ODD")
showNumbers(int(input("Enter the limit : ")))