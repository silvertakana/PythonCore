sentence = input("enter your sentence:\n")

words = sentence.split(" ")

longest_word = words[0]

for i in words:
    if(len(i) > len(longest_word)):
        longest_word = i

print(longest_word)
