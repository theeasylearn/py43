#create methods/function to convert one inch into another measurement units
#methods to convert inches into feet, meter, km etc 
def toFeet(inches):
    feet = inches / 12
    return feet 

def toMeter(inches):
    meter = inches / 39.37
    return meter

def toKM(inches):
    km = inches / 39370
    return km 
