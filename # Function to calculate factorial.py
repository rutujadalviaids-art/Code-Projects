# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


# Get input from the user
num = int(input("Enter a number: "))

# Display the result
print(f"The factorial of {num} is {factorial(num)}")