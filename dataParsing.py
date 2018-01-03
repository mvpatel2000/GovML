#dataParsing by Akhil

from queue import*
from collections import defaultdict

filepath = input("Enter Filename with extension: ")
file = open(filepath, "r")#, encoding='latin-1')

# 0 category, 1 subcategory, 2 lean rep%, 3 lean dem%, 4 indep%, 5 total num

category = ""

line = file.readline()
overall = []
while line != "":
	theLine = line.split(",")
	#print("The Line:", theLine)
	if theLine[0] == "":
		line = file.readline()
		continue

	category = theLine[0]
	subcategory = [theLine[1]]
	numRep = [float(theLine[2]) * float(theLine[5])]
	numDem = [float(theLine[3]) * float(theLine[5])]
	numIndep = [float(theLine[4]) * float(theLine[5])]
	
	line = file.readline()
	theLine = line.split(",")
	while(theLine[0] == category):
		#print("The Line:", theLine)
		subcategory.append(theLine[1])
		numRep.append(float(theLine[2]) * float(theLine[5]))
		numDem.append(float(theLine[3]) * float(theLine[5]))
		numIndep.append(float(theLine[4]) * float(theLine[5]))
		line = file.readline()
		theLine = line.split(",")

	#printing out the results
	print("Republican by ", category, ": ", sep="", end="")
	repTotal = 0;
	for k in numRep:
		repTotal += k
	for k in range(0, len(subcategory)):
		if k == len(subcategory) - 1:
			print("{0:.1%}".format(numRep[k] / repTotal), " ", subcategory[k], sep="")
		else:
			print("{0:.1%}".format(numRep[k] / repTotal), " ", subcategory[k], ", ", sep="", end="")

	print("Democrat by ", category, ": ", sep="", end="")
	demTotal = 0;
	for k in numDem:
		demTotal += k
	for k in range(0, len(subcategory)):
		if k == len(subcategory) - 1:
			print("{0:.1%}".format(numDem[k] / demTotal), " ", subcategory[k], sep="")
		else:
			print("{0:.1%}".format(numDem[k] / demTotal), " ", subcategory[k], ", ", sep="", end="")

	print("Independent by ", category, ": ", sep="", end="")
	indepTotal = 0;
	for k in numIndep:
		indepTotal += k
	for k in range(0, len(subcategory)):
		if k == len(subcategory) - 1:
			print("{0:.1%}".format(numIndep[k] / indepTotal), " ", subcategory[k], sep="")
		else:
			print("{0:.1%}".format(numIndep[k] / indepTotal), " ", subcategory[k], ", ", sep="", end="")
	print()

	#saving the results into "overall"
	subCatListRep = []
	for k in range(0, len(subcategory)):
		subCatListRep.append([subcategory[k], numRep[k] / repTotal])
	overall.append(["Republican by " + category, subCatListRep])

	subCatListDem = []
	for k in range(0, len(subcategory)):
		subCatListDem.append([subcategory[k], numDem[k] / demTotal])
	overall.append(["Democrat by " + category, subCatListDem])

	subCatListIndep = []
	for k in range(0, len(subcategory)):
		subCatListIndep.append([subcategory[k], numIndep[k] / indepTotal])
	overall.append(["Independent by " + category, subCatListIndep])

print(overall)