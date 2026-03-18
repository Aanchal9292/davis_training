def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

result = simple_interest(p, r, t)

print("Simple Interest:", result)