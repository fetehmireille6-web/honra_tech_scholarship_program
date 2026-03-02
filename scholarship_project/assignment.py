name = input("Enter your name:  ")
age = int(input("Enter your age:  "))
if age < 18:
    print("Sorry, you are not eligible for the scholarship.")
else:
    print(f"Congratulations, {name}! You are eligible for the scholarship.")