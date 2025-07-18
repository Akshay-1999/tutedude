def write_append_file(write_text,append_text):
    with open("output.txt",'w') as file:
        write_file = file.write(write_text)
        file.close
    with open("output.txt",'a') as file:
        append_file = file.write(append_text)
        file.close
    with open("output.txt","r") as file:
        read_file = file.read()
        return(read_file)
        file.close

if __name__=="__main__":
    write_text = input("enter the text you want to write into the file: ")
    append_text = input("enter the text you want to append into the file: ")  
    try:
        file_content = write_append_file(write_text,append_text)
        print(file_content)
    except Exception as e:
        print(f"some expection oocured :",{e})