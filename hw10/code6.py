class date:
	def __init__(self, day, month, year):
		#check valid day
		if day > 31 or day < 0:
			print("Invalid date")
			return
		if month > 12 or month < 0:
			print("Invalid month")
			return
		if year < 0:
			print("Invalid year")
			return
		self.day = day
		self.month = month
		self.year = year
	def __str__(self):
		return f"{self.day}/{self.month}/{self.year}"

class User:
	user_count = 0
	def __init__(self,first_name, last_name, birthday, email, address, username, password):
		self.is_logined = False
		self.login(first_name, last_name, birthday,
		           email, address, username, password)
	def __del__(self):
		User.user_count -= 1

	def login(self, first_name, last_name, birthday, email, address, username, password):
		if self.is_logined:
			print(f"user {self.first_name} {self.last_name} has not loged out yet. Please logout before logging in again.")
		else:
			self.first_name = first_name
			self.last_name = last_name
			self.birthday = birthday
			self.email = email
			self.address = address
			self.username = username
			self.password = password
			self.is_logined = True
			User.user_count += 1

	def logout(self):
		if self.is_logined:
			self.is_logined = False
			User.user_count -= 1
		else:
			print ("user already logged out.")

	def update_info(self, first_name=None, last_name=None, birthday=None, email=None, address=None, username=None, password=None):
		def check(x,y):
			if x != None:
				return x
			else: 
				return y
		self.first_name = check(first_name,self.first_name)
		self.last_name = check(last_name,self.last_name)
		self.birthday = check(birthday,self.birthday)
		self.email = check(email,self.email)
		self.address = check(address,self.address)
		self.username = check(username,self.username)
		self.password = check(password,self.password)


	def __str__(self):
		return f"\"{self.first_name} {self.last_name}\" \"{self.birthday}\" \"{self.email}\" \"{self.address}\" \"{self.username}\" \"{self.password}\""


silver = User("silvia","phung",date(16,12,2007),"titmitna@gmain.com", "93a foresthill","silvertakana","helloWorld123")
print(f"user: {silver}")

silver.update_info("silver")
print(f"user: {silver}")
print(User.user_count)
silver.logout()
print(User.user_count)
