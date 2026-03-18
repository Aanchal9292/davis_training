# function 
def discount_bill(price, discount):
    final_price = price - (price * discount / 100)
    print("Final price after discount:", final_price)
# taking input
price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

discount_bill(price, discount)