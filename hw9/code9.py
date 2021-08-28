your_sentence = input("enter your sentence>> ")
your_sentence_words = your_sentence.split(" ")

words_dict = {}
for word in your_sentence_words:
	if(word in words_dict):
		words_dict[word]+= 1
	else:
		words_dict[word] = 1

print(words_dict)
