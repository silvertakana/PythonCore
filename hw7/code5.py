my_list = [1,2,3,2,9,7,95,3,5,7,6,64,3,5,8]

list_components = []
components_appearence_counts = []

for i in my_list:
    if i in list_components:
        components_appearence_counts[list_components.index(i)] += 1
    else:
        list_components.append(i)
        components_appearence_counts.append(0)

smallest_index = 0

for i in components_appearence_counts:
    if i > components_appearence_counts[smallest_index]:
        smallest_index = components_appearence_counts[i]

print(list_components[smallest_index])
