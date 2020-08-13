def driver_speed(speed):
    point=(speed-70)/5 #counts demerit point
    if speed<=70:
        print("Speed is OK.")
    elif point>12:
        print("Your License is suspended")
    else:
        print("Points :",point)
driver_speed(int(input("Enter Drivers speed : ")))