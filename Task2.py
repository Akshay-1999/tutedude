def greet(first_name, last_name):
    """
    Greets the user with their full name.
    
    Parameters:
    first_name (str): The user's first name.
    last_name (str): The user's last name.
    
    Returns:
    str: A greeting message.
    """
    return f"Hello, {first_name} {last_name}! welcome to the Python program."

def main():
    """
    Main function to demonstrate the usage of the greet function.
    """
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    print(greet(first_name, last_name))

if __name__ == "__main__":
    main()