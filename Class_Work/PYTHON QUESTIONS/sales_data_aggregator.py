# 5. Sales Data Aggregator
# Given file:
# product,category,price,quantity
# Tasks:
# • Total sales per category
# • Highest selling product
# • Handle invalid rows 


category_sales = {}         # Dictionary to store total sales per category
max_product = ("", 0)       # Tuple to store highest selling product

# Open sales file
with open("sales.txt", "r") as file:
    for line in file:
        try:
            # Split line into fields
            product, category, price, qty = line.strip().split(",")

            # Convert price and quantity
            price = float(price)
            qty = int(qty)

            # Calculate total sales
            total = price * qty

            # Add to category total
            category_sales[category] = category_sales.get(category, 0) + total

            # Check for highest selling product
            if total > max_product[1]:
                max_product = (product, total)

        except:
            # Handle invalid rows
            print("Invalid row skipped")

# Display results
print("Category Sales:", category_sales)
print("Top Product:", max_product)