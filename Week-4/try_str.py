def repeat_at_index(the_list, index):
    second_list = ( the_list[0:index] + ([the_list[index]]*index) + the_list[index+1:len(the_list)] )
    return second_list

myList = [2,3,4,5,5,2,1]
print(repeat_at_index(myList, 2))