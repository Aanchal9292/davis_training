# Function to calculate bill
def total_bill(items):
    total = 0
    for i in items:
        total += i
    return total

print(total_bill([100,200,300]))