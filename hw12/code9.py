def extract_characters(*files):
	characters = ""
	for file in files:
		f = open(file, "r")
		characters += f.read()
		f.close()
	return set(characters)


print(extract_characters("mytext.txt", "mytext2.txt", "mytext3.txt"))
