sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]

def get_keys(d,keys):
	return dict([(i,d[i]) for i in keys])
print(get_keys(sampleDict, keys))
