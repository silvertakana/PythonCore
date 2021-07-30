import json

print("please enter your id in this format: [a,b,c,d,e,f,g,h,i,j,k,l...]")
list_of_songs = input('all songs id>>')

list_of_songs = json.loads(list_of_songs)
all_songs = []
for i in list_of_songs:
    is_repeated = False
    for j in all_songs:
        if(i == j):
            is_repeated = True
            break
    if(not is_repeated):
        all_songs.append(i)
print(all_songs)
