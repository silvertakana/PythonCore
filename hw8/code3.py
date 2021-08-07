
mylist1 = ["apple", "banana", "cherry", "mango", "carrot", "peach"]
mylist2 = ["apple", "banana", "cherry",("fish","pig","cow","sheep"), "mango", "carrot", "peach"]

def a_weird_way_to_count(da_list):
    size = 0
    for i in da_list:
        if(isinstance(i,tuple)):
            break
        size+=1
    return size

print(a_weird_way_to_count(mylist1))
print(a_weird_way_to_count(mylist2))
