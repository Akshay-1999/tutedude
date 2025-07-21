def get_marks(marks,name):
    lower_name = name.lower()
    try:
        if lower_name in marks:
            name = lower_name
            marks = marks[lower_name]
            message = (f"the name of the student you entered is {name} and there marks are {marks}.")
            return(message)
        else:
            return("student not Found")
    except Exception as e:
        return(f"there was some exception",{e})

if __name__ == "__main__":
    name = input("enter the name of the student :")
    marks = {
        "alex":100,
        "max":90,
        "jhon":70
    }
    value = get_marks(marks,name)
    print(value)