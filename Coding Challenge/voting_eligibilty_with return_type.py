def check_vote(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

age = int(input("Enter age: "))
result = check_vote(age)
print(result)
