def discount_bill(price, discount):
    final_price = price - (price * discount / 100)
    print("Final price:", final_price)

price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

discount_bill(price, discount)