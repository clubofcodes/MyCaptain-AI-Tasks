def sumOfMul(limit):
    sum=0
    for n in range(0,limit+1):
        if n%3==0 or n%5==0:
            sum +=n         
    print("The sum of multiples of 3 & 5 till {} is {}.".format(limit,sum))
sumOfMul(int(input("Enter the limit : ")))