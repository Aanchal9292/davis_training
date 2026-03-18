units = float(input("Enter units: "))

bill = (units*5) if units<=100 else ((100*5)+(units-100)*7) if units<=200 else ((100*5)+(100*7)+(units-200)*10)

print("Total bill:", bill)