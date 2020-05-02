#Python 3
#Nolan Aubuchon
'''
Tests the Collatz Conjecture
Writes the output to 'collatz.txt'
'''

def printCollatz(num = 1):
	if(num == 1):
		return "1"
	elif(num % 2 == 0):
		return str(int(num)) + " -> " + printCollatz(num/2)
	else:
		return str(int(num)) + " -> " + printCollatz(num * 3 + 1)

file = open("collatz.txt","w")
for i in range(1,1000):
        file.write(str(printCollatz(i)) + "\n")
        
file.close()
#end
