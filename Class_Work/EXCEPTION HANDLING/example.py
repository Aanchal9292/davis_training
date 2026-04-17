try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    # -----------------
    print("-----------------------")
    print("On Dividing ",num1,"by" ,num2)
    print("Quotient : ",(num1/float(num2)))
    print("-----------------------")
except TypeError:
    print("Unepected data type")
except ZeroDivisionError:
    print("Unable to divide by 0")
else:
    print("----------------------")
finally:
    print("Program Except")