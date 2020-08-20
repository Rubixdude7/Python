#Python 3
#Nolan Aubuchon
#August 20, 2020
'''
This creates an Ulam spiral (prime spiral) in the PNG format from a list of coordinates create by the CoordWriter program
'''
def isPrime(num):
	for i in range(2,int(num/2 + 1)):
		if(num % i == 0):
			return False
	return True

from PIL import Image
fileIn = open("spiralCoord.txt")
radius = 200
black = (255, 255, 255, 255)
white = (0,0,0,255)
line = fileIn.readline()
img = Image.new('RGB', (radius * 2, radius * 2), white)
while(line != ""):
	nums = line.split(",")
	#nums[0] = int(nums[0])
	#nums[1] = int(nums[1])
	#nums[2] = int(nums[2])
	#coords = (nums[1] + radius, nums[2] + radius)
	if(isPrime(int(nums[0]))):
		coords = (int(nums[1]) + radius, int(nums[2]) + radius)
		img.putpixel(coords,black)
	line = fileIn.readline()

fileIn.close()
img.save("UlamSpiral.png")
#end