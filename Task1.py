def add(num1,num2):
    """
    This function takes two numbers as input and returns their sum.
    
    Parameters:
    num1 (int or float): The first number to add.
    num2 (int or float): The second number to add.
    
    Returns:
    int or float: The sum of num1 and num2.
    """
    return (num1 + num2)

def subtract(num1,num2):
    """
    This function takes two numbers as input and returns their difference.
    
    Parameters:
    num1 (int or float): The number from which to subtract.
    num2 (int or float): The number to subtract from num1.
    
    Returns:
    int or float: The difference of num1 and num2.
    """
    return (num1 - num2)

def multiply(num1,num2):
    """
    This function takes two numbers as input and returns their product.
    
    Parameters:
    num1 (int or float): The first number to multiply.
    num2 (int or float): The second number to multiply.
    
    Returns:
    int or float: The product of num1 and num2.
    """
    return (num1 * num2)

def divide(num1,num2):
    """
    This function takes two numbers as input and returns their quotient.
    
    Parameters:
    num1 (int or float): The numerator.
    num2 (int or float): The denominator.
    
    Returns:
    float: The quotient of num1 divided by num2.
    
    Raises:
    ValueError: If num2 is zero, as division by zero is not allowed.
    """
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return (num1 / num2)

def main():
    """
    Main function to demonstrate the usage of the arithmetic functions.
    """
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide(num1, num2))

if __name__ == "__main__":
    main()