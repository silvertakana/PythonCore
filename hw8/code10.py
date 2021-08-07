
my_websites = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]

my_websites_suffix = [i.split(".")[-1] for i in my_websites]
my_websites_suffix = tuple(my_websites_suffix)
print(my_websites_suffix)
