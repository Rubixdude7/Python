#python 3
#Kruskal's Algorithm
from Matrix import Matrix
from random import random
a = None
b = 0
sum = 0
flags = [0,0,0,0,0,0,0]
matrix = Matrix( [a,7,a,5,a,a,a] , [a,a,8,9,7,a,a] , [a,a,a,a,5,a,a] , [a,a,a,a,15,6,a] , [a,a,a,a,a,8,9] , [a,a,a,a,a,a,11] , [a,a,a,a,a,a,a] )
SIZE = matrix.size()
i = 1
while(i < SIZE): #n vertices --> (n-1) edges
	edge = matrix.min()
	x = edge[0]
	y = edge[1]
	weight = edge[2]
	if(flags[x] == 0 or flags[y] == 0):
		if(flags[x] == 0 and flags[y] == 0):
			b = random()
		elif(flags[x] == 0):
			b = flags[y]
		else:
			b = flags[x]
		flags[x] = b
		flags[y] = b
		sum += weight
		matrix.set(x,y,a) #y is always greater than x
		print(str(edge) + " -- %d\n" % i)
		i += 1
	elif(flags[x] != flags[y]): #joining the two systems
	     for j in range(len(flags)):
		     if(flags[j] == flags[y]):
			     flags[j] = flags[x]
	     sum += weight
	     matrix.set(x,y,a)
	     print(str(edge) + " -- %d\n" % i)
	     i += 1
	else:
	     matrix.set(x,y,a)
print("minimum cost: %d" % sum)
