name_ids = {
	"TAcHicepTioUsH": 1283,
	"RtuatlEnthAINi": 1231,
	"OTeaMiSetRIshi": 2712,
	"dreMNAlEARACKL": 5629,
	"SiTiTUstELeTIc": 8572
}
a = list(name_ids.items())

a.sort(key = lambda x: x[1])

for i in a[-3:]:
	print(i)
