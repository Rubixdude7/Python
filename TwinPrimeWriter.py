def isPrime(num):
	for i in range(2,int(num/2 + 1)):
		if(num % i == 0):
			return False
	return True
	
file = open("twinPrimes.txt","w")
for i in range(3,10000,2):
	if(isPrime(i)):
		if(isPrime(i+2)):
			file.write(str(i) + ", " + str(i+2) + "\n")
file.close()
