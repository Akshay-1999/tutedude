def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for index, line in enumerate(lines, start=1):
                print(f"Line {index}: {line.strip()}")
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")


if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    read_file(file_name)