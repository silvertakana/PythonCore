the_object =  [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

a = {}

for i in the_object:
	if(i['item'] in a):
		a[i['item']] += i['amount']
	else:
		a[i['item']] = i['amount']

print(a)
