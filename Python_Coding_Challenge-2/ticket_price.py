# Function to determine ticket price
def ticket_price(day):
    if day == "Sunday":
        return 200
    else:
        return 150

day = input("Enter day: ")
print(ticket_price(day))