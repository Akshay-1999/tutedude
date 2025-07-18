class file_handling:
    def write_file(self,write_text):
        try:
            with open("output.txt", "w") as file:
                file_write = file.write(write_text)
                file.close
            return(write_text)
        except Exception as e:
            print(f"some error happend : ",{e})
    def append_file(self,append_content):
        try:
            with open("output.txt","a") as file:
                file_append = file.write(append_content)
                file.close
            return(append_content)
        except Exception as e:
            print(f"there are some exception :",{e})
    def read_file(self):
        try:
            with open("output.txt","r") as file:
                file_content = file.read()
                file.close
            return(file_content)
        except Exception as e:
            print(f"there is some exception :",{e})

if __name__=="__main__": 
    file_obj = file_handling()
    try:
        write_text = input("enter the text you want to write into the file: ")
        file_write = file_obj.write_file(write_text)
        print("Data written successfully written to output.txt")
        append_text = input("enter the text you want to append into the file: ") 
        file_append = file_obj.append_file(append_text)
        print("Data append successfully written to output.txt")
        file_content = file_obj.read_file()
        print("the content of the output.txt : ", file_content ,sep = "\n")
    except Exception as e:
        print(f"some expection oocured :",{e})