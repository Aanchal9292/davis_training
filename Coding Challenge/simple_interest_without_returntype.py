def simple_interest(p, r, t):
    si = (p * r * t) / 100
    print("Simple Interest:", si)

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

simple_interest(p, r, t)