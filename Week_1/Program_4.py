# Accept input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check for division by zero
if num2 == 0:
    print("Error: Cannot divide by zero.")
else:
    result = num1 / num2
    print("The result of the division is:", result)
