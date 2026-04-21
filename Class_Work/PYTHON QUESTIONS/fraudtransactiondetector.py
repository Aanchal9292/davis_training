# 2. Fraud Transaction Detector
# Given a list of transactions:
# • Detect suspicious ones based on:
# o Amount > threshold
# o Same user multiple transactions within short time
# Use:
# • loops + conditions
# • Store flagged data in dictionary 

# List of transactions (user, amount)
transactions = [
    ("user1", 5000),
    ("user2", 15000),
    ("user1", 7000),
    ("user3", 20000)
]

threshold = 10000      # Amount above which transaction is suspicious
flagged = {}           # Dictionary to store suspicious transactions
user_count = {}        # Dictionary to count transactions per user

# Loop through each transaction
for user, amount in transactions:

    # Check if amount exceeds threshold
    if amount > threshold:
        # Store suspicious transaction
        flagged[user] = flagged.get(user, []) + [amount]

    # Count number of transactions per user
    user_count[user] = user_count.get(user, 0) + 1

# Check for multiple transactions
for user, count in user_count.items():
    if count > 2:
        flagged[user] = "Multiple transactions"

# Display flagged transactions
print("Flagged Transactions:", flagged)