set1 = {1,2,3,4}
set2 = {4,5,6,7}

# set1.difference_update(set2)
set1 = set1 - set2

print(set1)

set1 = {1,2,3,4}
set2 = {4,5,6,7}

# set1.intersection_update(set2)
set1 = set1 & set2

print(set1)

set1 = {1,2,3,4}
set2 = {4,5,6,7}

# set1.isdisjoint(set2)

print((set1 & set2) == set())

set1 = {1,2,3,4}
set2 = {1,2,3}

# set1.issubset(set2)

print((set1 - set2) == set())

set1 = {1,2,3,4}
set2 = {1,2,3}

# set1.issuperset(set2)

print((set2 - set1) == set())

set1 = {1,2,3,4}
set2 = {4,5,6,7}

# set1.intersection_update(set2)
set1 = set1 ^ set2

print(set1)
