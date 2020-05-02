#Python 3
#Nolan Aubuchon
'''
Converts 'collatz.txt' output by Collatz.py into a format that can be opened by Excel
'''

def countArrow(s = ""):
	total = 0
	for i in range(len(s)):
		if(s[i:i+2] == "->"):
			total += 1
	return total

fileIn = open("collatz.txt")
fileOut = open("collatzToExcel.txt","w")
line = fileIn.readline()
count = 1
while(line != ""):
	fileOut.write("%d;%d\n" % (count,countArrow(line)))
	line = fileIn.readline()
	count += 1

fileIn.close()
fileOut.close()
#end