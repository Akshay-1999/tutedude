def list_split(list):
    split_list = list[0:5]
    return(split_list)
def reverse_list(list_split):
    list_split.reverse()
    return(list_split)

if __name__ =="__main__":
    list = [i**1 for i in range(1,11)]
    a = reverse_list(list_split(list))
    b = list_split(list)
    print(b)
    print(a)