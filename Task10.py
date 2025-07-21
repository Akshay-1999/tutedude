class list_function:
    def splitlist(self,list):
        try:    
            length = len(list)
            split = (length/2)
            split_list = list[0:int(split)]
            return(split_list)
        except Exception as e:
            return(e)

if __name__ =="__main__":
    list_obj = list_function()
    list = [i*1 for i in range(1,11)]
    split_list= list_obj.splitlist(list)
    print("the original list is : ",list)
    print("the split list is : ",split_list)
    split_list.reverse()
    print("reversed list is : ",split_list)