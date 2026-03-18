# taking input from user
price = float(input("Enter the price : "))
discount = float(input("Enter the discount(in %): "))
# Calculating discount amount
discount_amount = (price * discount) / 100
# calculating final price
final_price = price - discount_amount
print("Final price is : ",final_price)