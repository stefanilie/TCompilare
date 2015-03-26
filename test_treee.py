arrPrintElements=[]

class Tree:
	def __init__(self):
		self.value=None
		self.left=None
		self.right=None

	def print_tree(self):
		if self.value!=None:
			self.left.print_tree()
			arrPrintElements.append(self.value)
			self.right.print_tree()

	def addElement(self, value):
		print 'sunt in fucntie'
		if self.value==None and self.left==None and self.right==None:
			print 'in primul if'
			self.value=value
			self.left = [Tree() for i in range(10)]
			self.right = Tree()
		elif value % 2 != 0:
			self.left.addElement(value)
		elif value %2 ==0:
			self.right.addElement(value)

def main():
	root = Tree()
	for i in range(10):
		root.addElement(i)

	root.print_tree()
	print arrPrintElements


if __name__ == "__main__":
    main()