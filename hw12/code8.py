def get_file_size(file):
	readFile = open(file,"r")
	size = len(readFile.read())	
	readFile.close()
	return size

print(get_file_size("mytext3.txt"))
