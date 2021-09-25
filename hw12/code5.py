n = input("n>>")

textFile = open("mytext.txt", "r")
print(textFile.read(n))
textFile.close()
