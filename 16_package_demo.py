#import two modules 
# currency module
# import package-name.sub-package-name.filename
import converter.currency.money as mn 
# measure module
import converter.unit.measure as ms 
rupees = int(input("Enter indian rupees to convert it into dollar, euro, pound"))

print("Dollar = ",mn.toDollar(rupees))
print("Euro = ",mn.toEuro(rupees))
print("British pound =",mn.toPound(rupees))

inches = int(input("Enter inches to convert it into feet, meter, kilo meter"))
print("feet = ",ms.toFeet(inches))
print("meter = ",ms.toMeter(inches))
print("km = ",ms.toKM(inches))

