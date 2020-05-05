def isPrime(num):
	for i in range(2,int(num/2 + 1)):
		if(num % i == 0):
			return False
	return True
	
file = open("primes.txt","w")
file.write("2\n")
for i in range(3,10000,2):
	if(isPrime(i)):
		file.write(str(i) + "\n")
file.close()
