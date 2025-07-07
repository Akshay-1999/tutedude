import math
def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(x)
def natural_logarithm(x):
    if x <= 0:
        raise ValueError("Natural logarithm is not defined for non-positive numbers")
    return math.log(x)
def sine(x):
    return math.sin(x)

if __name__ == "__main__":
    try:
        x = float(input("Enter a non-negative number for square root: "))
        print(f"The square root of {x} is {square_root(x)}")
        
        print(f"The natural logarithm of {x} is {natural_logarithm(x)}")
        
        print(f"The sine of {x} radians is {sine(x)}")
        
    except ValueError as e:
        print(e)