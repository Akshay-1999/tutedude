class file_operation:
    def write_file(self,write_text):
        with open("sample.txt",'w') as file:
            file_write = file.write(write_text)
            file.close

if __name__ == "__main__":
    obj = file_operation()
    write_text = input("enter text : ")
    try:
        obj.write_file(write_text)
    except Exception as e:
        print(f"there is an exception : ",{e})