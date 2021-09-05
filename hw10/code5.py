class NewString:
	def get_string(self, string):
		self.string = string
	def print_string(self):
		print(self.string.upper())

string = NewString()
string.get_string(input("your string >>"))
string.print_string()
