def find_x1(list,x):
  for i in range(len(list)):
    if list[i] == x:
      return i
  return -1
def find_x2(list,x):
  return list.index(x)

my_list = [12312,12,3,41,2,41,2,1,2,54,4,5,123,65,12,3,1241,2,3,12,3]
print(find_x1(my_list,1241))
print(find_x2(my_list,1241))
