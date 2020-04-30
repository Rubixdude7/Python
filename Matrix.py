import sys
class Matrix:

	def __init__(self,*args):
		self.matrix = list(args)
		
	def get(self, i = 0, j = 0):
		return self.matrix[i][j]
		
	def set(self, i = 0, j = 0, value = 0):
		self.matrix[i][j] = value
		
	def size(self):
		return len(self.matrix)
		
	def min(self):
		if(self.size() == 0):
			return (0, 0, None)
		a = 0
		b = 0
		min = sys.maxsize
		for i in range(self.size()):
			for j in range(self.size()):
				if(self.matrix[i][j] != None and self.matrix[i][j] < min):
					min = self.matrix[i][j]
					a = i
					b = j
		return (a, b, min)
		
	def addRow(self,row):
		self.matrix.append(row)
	
		
	def __str__(self):
		string = ""
		for line in self.matrix:
			string += str(line) + "\n"
		return string[:-1] #deletes last newline character
