name_ids = {
	"TAcHicepTioUsH": 1283,
	"RtuatlEnthAINi": 1231,
	"OTeaMiSetRIshi": 2712,
	"dreMNAlEARACKL": 5629,
	"SiTiTUstELeTIc": 8572
}
#medthod 1
minimum = float('inf')
maximum = float('-inf')
for i in name_ids:
	n = name_ids[i]
	if(n > maximum): maximum = n
	if(n < minimum): minimum = n

print(maximum,minimum)

#medthod 2
print(max(name_ids.values()),min(name_ids.values()))
