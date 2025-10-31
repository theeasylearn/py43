# write a program to findout Strike rate of batsman in cricket using given runs and balls 
while 1!=2:
    try:
        runs = int(input("Enter batter's run"))
        balls = int(input("Enter batter's ball played"))
        #calculate strike rate (how many runs per ball batter has made, more run per ball means batter is good )
        strike_rate = runs/balls
        print(f"strike rate = {strike_rate}")
        break #it will stop loop inbetween
    except ZeroDivisionError:
        print("Error, input can not be zero")
    except ValueError:
        print("Error, input can be only numbers")

print("thanks for using our program")