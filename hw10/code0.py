class player:
	def __init__(self,name,id):
		self.name = name
		self.id = id
	def generate_username(self):
		return f"{self.name}#{self.id}"

silver = player("silver", 69)

print(silver.generate_username())
print(type(silver))
