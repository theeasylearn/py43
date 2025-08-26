import unit_converter as unit 

kms = int(input("Enter KM"))
miles = int(input("Enter Miles"))


result = unit.toKM(miles)
print(f"km of {miles} = {result}")

result2 = unit.toMiles(kms)
print(f"miles of {kms} = {result2}")


