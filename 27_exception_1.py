# write a program to findout Strike rate of batsman in cricket using given runs and balls 
try:
    runs = int(input("Enter batter's run"))
    balls = int(input("Enter batter's ball played"))
    #calculate strike rate (how many runs per ball batter has made, more run per ball means batter is good )
    strike_rate = runs/balls
except ZeroDivisionError:
    print("Error, input can not be zero")
except ValueError:
    print("Error, input can be only numbers")
else:
    print(f"strike rate = {strike_rate}")
finally:
    print("thanks for using our program")