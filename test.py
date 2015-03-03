import auto
	
auto.initialise("data.txt")
result= auto.autocomplete("de")

for line in result:
	print line
