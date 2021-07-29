my_list = [1,2,3,2,9,7,95,3,5,7,6,64,3,5,8]

first_list_length = int(input("first_list_length>> "))
if first_list_length > len(my_list):
    print("the first list length is too long. the program will stop")

print({"list 1": my_list[0:first_list_length],"list 2": my_list[first_list_length:len(my_list)]})
