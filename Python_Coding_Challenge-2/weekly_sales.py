# Function to calculate weekly sales
def weekly_sales(sales):
    total = 0
    for i in sales:
        total += i
    return total

sales = [100,200,150,300,250,400,100]

print(weekly_sales(sales))