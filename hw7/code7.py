list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
is_collided = False
for i in list1:
    for j in list2:
        if i == j:
            is_collided = True
            break
    if is_collided:
        break
print(is_collided)
