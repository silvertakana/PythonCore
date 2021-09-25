
f = open("mytext3.txt", "w")
f1 = open("mytext.txt", "r")
f2 = open("mytext2.txt", "r")

f.write(f1.read()+f2.read())

f.close()
f1.close()
f2.close()
