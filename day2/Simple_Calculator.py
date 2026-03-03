num1 = int(input("Enter a number of your choice:  "))
num2 = int(input("Enter a second number of your choice:  "))
operator = (input("Enter an operator of your choice:  "))
if operator == "+":
    print(f"The answer of {num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"The answer of {num1} - {num2} = {num1 - num2}")
elif operator == "/":
    print(f"The answer of {num1} / {num2} = {num1 / num2}")
else:
    print(f"The answer of {num1} * {num2} = {num1 * num2}")


