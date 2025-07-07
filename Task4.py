def sumfirst_n(n):
    """
    Calculate the sum of the first n natural numbers.
    
    :param n: The number of natural numbers to sum.
    :return: The sum of the first n natural numbers.
    """
    for i in range(1, n + 1):
        if i == 1:
            total = i
        else:
            total += i
    return total

def main():
    """
    Main function to demonstrate the usage of the sumfirst_n function.
    """
    try:
        n = int(input("Enter a positive integer: "))
        if n < 1:
            raise ValueError("Please enter a positive integer.")
        result = sumfirst_n(n)
        print(f"The sum of the first {n} natural numbers is {result}.")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()