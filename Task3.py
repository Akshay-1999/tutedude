def checkevenodd(num):
    """
    This function checks if a number is even or odd.
    
    :param num: The number to check
    :return: 'even' if the number is even, 'odd' if the number is odd
    """
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'

def main():
    """
    Main function to demonstrate the usage of the checkevenodd function.
    """
    try:
        num = int(input("Enter a number: "))
        result = checkevenodd(num)
        print(f"The number {num} is {result}.")
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()