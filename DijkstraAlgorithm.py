#Python 3
#Nolan Aubuchon
#Dijkstra's Algorithm

'''
Still needs work, but nonetheless is a proof of concept
Note: the leftmost entry of the matrix is the starting position. The furthest right is the goal

With the given graph.txt file the output is:
minimum cost: 8

0 -> 4 -> 5 -> 6 -> 7
'''
from Matrix import Matrix
from pathstring import pathstring
matrix = Matrix()
blank = Matrix()

file = open("graph.txt")
string = file.readline()
while(string != ""):
	matrix.addRow(eval(string))
	string = file.readline()

size = matrix.size()
flags = [None] * size
paths = [None] * size
flags[0] = 0;
count = 1
for i in range(size):
	blank.addRow([None] * size)

while(flags[-1] == None):
	for i in range(size):
		for j in range(i+1,size):
			if(flags[i] != None and matrix.get(i,j) != None and 
			matrix.get(i,j) + flags[i] <= count and 
			(flags[j] == None or flags[j] > flags[i] + matrix.get(i,j))):
				flags[j] = flags[i] +matrix.get(i,j)
				paths[j] = i
				blank.set(i,j,matrix.get(i,j))
				blank.set(j,i,matrix.get(i,j))
	count += 1
file.close()

print("minimum cost: %d\n" % flags[-1])
print(pathstring(paths))
input()

def pathstring(a = [0], index = -1):
	if(index == 0):
		return "0"
	elif(index == -1):
		return pathstring(a,a[index]) + " -> " + str(len(a)-1)
	else:
		return pathstring(a,a[index]) + " -> " + str(index)

#end	
