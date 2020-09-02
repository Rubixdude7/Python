file = open("LychrelNumberResults.txt","w")
for i in range(10,196):
	total = i
	while(str(total) != str(total)[::-1]):
		file.write("%i, " % total)
		total += int(str(total)[::-1])
	file.write("%i\n" % total)
file.close()
