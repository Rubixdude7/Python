#python

def factorial(n):
	if(n==1 or n==0):
		return 1
	return n*factorial(n-1)
	
num = eval(input("Enter a number: "))
print(factorial(num))
input("Press enter to continue...")
