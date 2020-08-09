import csv
with open ('/Users/aandrejevic/downloads/data-2.csv') as f:
	csv_reader = csv.DictReader(f)

	yes = 0.0
	no = 0.0

	for line in csv_reader:
		#print(line['out:Standard Effective Temperature [C]'])
		#print(line)
		#break
		if line ['out:Standard Effective Temperature [C]'] > '20':
			yes += 1
		elif line ['out:Standard Effective Temperature [C]'] < '20':
			no += 1

total = (yes + no)

#print(total)
#print(yes)
#print(no)

yes_prct = (yes / total) * 100

no_prct = (no / total) * 100

yes_prct = round(yes_prct, 1)
no_prct = round(no_prct, 1)

print (yes_prct)
print (no_prct)

#print(yes_prct)
#print(no_prct)
		

		

