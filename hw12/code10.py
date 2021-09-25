for i in range(26):
	f = open(f"26_text_files/{chr(i+65)}.txt","w")
	f.write(chr(i+65))
	f.close()
