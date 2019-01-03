#python
class LinkedList:

	def __init__(self, key = 0, data = None, nextNode = None):
		self.key = key
		self.data = data
		self.nextNode = nextNode
		
	def add(self, data):
		if(self.nextNode == None):
			self.nextNode = LinkedList(self.key + 1, data, None)
		else:
		    self.nextNode.add(data)
		
	def get(self, index):
		if(self.key == index):
			return self.data
		else:
			return self.nextNode.get(index)
	
	def size(self, i = 0):
		if(self.data == None and self.nextNode == None):
			return i
		elif(self.data != None and self.nextNode == None):
			return i+1
		else:
			return self.nextNode.size(i+1)
			
			
myList = LinkedList(data = "Hydrogen")
print ("size of list: ", myList.size())
myList.add(data = "Helium")
print ("size of list: ", myList.size())
myList.add(data = "Lithium")
print ("size of list: ", myList.size())
for i in range(3):
        print (myList.get(i))
