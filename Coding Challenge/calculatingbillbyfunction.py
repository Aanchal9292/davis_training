def calculatingbill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    return bill

# Electricity bill calculator
units = float(input("Enter number of units consumed: "))

bill = calculatingbill(units)   # calling the function

print("Total bill is: Rs.", bill)