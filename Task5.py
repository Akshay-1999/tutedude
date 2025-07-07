def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
if __name__ == "__main__":
    try:
        n = int(input("Enter a non-negative integer to calculate its factorial: "))
        if n < 0:
            raise ValueError("Please enter a non-negative integer.")
        result = factorial(n)
        print(f"The factorial of {n} is {result}.")
    except ValueError as e:
        print(e)