# this is module which has method to convert one measurement unit's value into another measurement unit's value 
# miles, KM, Liter, KG, Pounds 
# miles = 0 # global variable
def toMiles(km):
    #miles is local variable (available to access only inside toMiles)
    miles = km / 1.609
    return miles
def toKM(miles):
    km = miles * 1.609
    return km 

