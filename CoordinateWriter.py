#Nolan Aubuchon
#Python 3
#August 19, 2020

"""
This program writes coordinates to a text file in order to generate an Ulam spiral (prime number spiral) with another python program)
"""


def nextCoord(coords2):
	x = coords2[0]
	y = coords2[1]
	if(x == 0 and y == 0):
		return (1,0)
	elif(x > 0 and y > 0 and x == y):
		x-=1
	elif(abs(x) == abs(y) and y > x):
		y-=1
	elif(x < 0 and y < 0 and x == y):
		x+=1
	elif(abs(x) == abs(y) and x > y):
		x+=1
	elif(abs(x) > abs(y) and x > 0):
		y+=1
	elif(abs(x) > abs(y) and x < 0):
		y-=1
	elif(abs(x) < abs(y) and y > 0):
		x-=1
	elif(abs(x) < abs(y) and y < 0):
		x+=1
	else:
		print("This text should not appear")
	return (x,y)


coords = (0,0)
file = open("spiralCoord.txt","w")
file.write("0, %i, %i\n" % coords)
for i in range(1,1000,1):
	coords = nextCoord(coords)
	file.write("%i, %i, %i\n" % (i,coords[0],coords[1]))
file.close()
