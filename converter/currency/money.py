#create methods/function to convert one currency into another
#methods to convert rupees into dollar, euro, pound etc 

def toDollar(rupees):
    #local variable
    dollar = rupees / 88.7
    return dollar

def toEuro(rupees):
    euro = rupees / 103.58
    return euro

def toPound(rupees):
    pound = rupees / 118.45
    return pound
