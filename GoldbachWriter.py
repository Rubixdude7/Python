def isPrime(num):
	for i in range(2,int(num/2 + 1)):
		if(num % i == 0):
			return False
	return True
	
file = open("GoldbachSums.txt","w")
flag = False
for i in range(4,1000,2):
	for j in range(2,int(i/2+1)):
		if(not flag and isPrime(j) and isPrime(i-j)):
			file.write("%i = %i + %i" % (i,j,i-j))
			flag = True
		elif(flag and isPrime(j) and isPrime(i-j)):
			file.write(", %i + %i" % (j,i-j))
		if(flag and j == int(i/2+1) - 1):
			file.write("\n")
	flag = False
file.close()