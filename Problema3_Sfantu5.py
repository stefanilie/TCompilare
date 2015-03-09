#3. Sa se scrie un program care primeste la intrare elementele 
#unei expresii regulate (alfabetul expresiei, expresia propriuzisa 
#(in forma prefixata sau infixata - adica forma naturala), care contine 
#3 tipuri de operatori: reuniune, concatenare si iteratie Kleene (*)). 
#Sa se determine un automat finit determinist (sa se afiseze elememtele 
#sale) care recunoaste acelasi limbaj ca cel descris de expresia regulata,
#folosind algoritmul de la curs.
#(bba|aa)*(a|b)*

#todo: beautify read text so that ' ' can be cleaned
import sys
arrPrintElements=[]
arrNumbers=[]
counter=1
class Tree:
	def __init__(self):
		self.left=None
		self.right=None
		self.strValue=None
		self.bNullable = None
		self.nCount =None
		self.arrFirstPos=[]
		self.arrLastPos=[]
		self.arrFollowPos=[]

	def addElement(self, value, bIsLettter=False):
		if self.strValue==None:
				self.strValue = value
				self.right = Tree()
				self.left = Tree()
		elif bIsLettter and self.right.strValue==None:
			self.right.addElement(value, True)
		elif bIsLettter and self.right.strValue!=None:
			self.left.addElement(value, True)
		elif not bIsLettter:
			self.left.addElement(value, False)

	def print_tree(self):
		if self.strValue!=None:
			arrPrintElements.append(self.strValue)
			arrNumbers.append(self.nCount)
			self.left.print_tree()
			self.right.print_tree()
			
	def addNumbers(self):
		global counter
		if self.strValue!=None:
			self.left.addNumbers()
			if self.left.strValue==None and self.right.strValue==None:
				self.nCount = counter
				counter+=1
			elif self.strValue == '|' or self.strValue=='*' or self.strValue=='.':
				self.nCount=0
			print 'sunt in nodul '+self.strValue+' si am counter='+str(self.nCount)+' si left= '+str(self.left.strValue)+' si right='+str(self.right.strValue)
			self.right.addNumbers()

	def nullable(self, count):
		if self.nCount == count:
			if self.strValue=='^':
				return True
			else:
				return False
		elif self.strValue=='|':
			if self.left.strValue!=None and self.right.strValue!=None:
				return self.left.nullable(self.left.nCount) or self.right.nullable(self.right.nCount)
		elif self.strValue=='.':
			if self.left.strValue!=None and self.right.strValue!=None:
				return self.left.nullable(self.left.nCount) and self.right.nullable(self.right.nCount)
		elif self.strValue=='*':
			if self.left.strValue!=None and self.right.strValue==None:
				return self.left.nullable(self.left.nCount)
			elif self.left.strValue==None and self.right.strValue!=None:
				return self.right.nullable(self.right.nCount)

	def firstPos(self, count):
		if self.nCount==count:
			if self.strValue=='^':
				return None
			else: 
				#sigur aici e asa?
				return self.nCount
		elif self.strValue=='|':
			if self.left.strValue!=None and self.right.strValue!=None:
				self.arrFirstPos.append(self.left.firstPos(self.left.nCount))
				self.arrFirstPos.append(self.right.firstPos(self.right.nCount))
				return self.arrFirstPos
		elif self.strValue=='.':
			if self.left.strValue!=None and self.right.strValue!=None:
				if self.left.nullable(self.left.nCount):
					self.arrFirstPos.append(self.left.firstPos(self.left.nCount))
					self.arrFirstPos.append(self.right.firstPos(self.right.nCount))
					return self.arrFirstPos
				else:
					return self.arrFirstPos.append(self.left.firstPos)
		elif self.strValue=='*':
			if self.left.strValue!=None and self.right.strValue==None:
				return self.left.firstPos(self.left.nCount)
			elif self.left.strValue==None and self.right.strValue!=None:
				return self.right.firstPos(self.right.nCount)

	def lastPos(self, count):
		if self.nCount==count:
			if self.strValue=='^':
				return None
			else: 
				#sigur aici e asa?
				return self.nCount
		elif self.strValue=='|':
			if self.left.strValue!=None and self.right.strValue!=None:
				self.arrLastPos.append(self.left.lastPos(self.left.nCount))
				self.arrLastPos.append(self.right.lastPos(self.right.nCount))
				return self.arrLastPos
		elif self.strValue=='.':
			if self.left.strValue!=None and self.right.strValue!=None:
				if self.left.nullable(self.left.nCount):
					self.arrLastPos.append(self.left.lastPos(self.left.nCount))
					self.arrLastPos.append(self.right.lastPos(self.right.nCount))
					return self.arrLastPos
				else:
					return self.arrLastPos.append(self.right.lastPos)
		elif self.strValue=='*':
			if self.left.strValue!=None and self.right.strValue==None:
				return self.left.lastPos(self.left.nCount)
			elif self.left.strValue==None and self.right.strValue!=None:
				return self.right.lastPos(self.right.nCount)

	#refa followPos cu caietul
	def followPos(self, count):
		if self.strValue=='.':
			if self.left.strValue!=None and self.right.strValue!=None:
				self.left.lastPos(self.left.nCount)
				for i in range(len(self.left.arrLastPos)):





def parseAlphabet(inputed):
	isInputed = inputed
	if ',' in isInputed:
		isInputed = isInputed.split(',')
	return isInputed

def checkExpression(expression, alphabet):
	for i in range(len(expression)):
		if expression[i] not in ['(', ')', '*', '|', '.', ' ']:
			if expression[i] not in alphabet:
				return False
	return True

def buildTree():
	root = Tree()
	root.addElement('.')
	root.addElement('#', True)
	root.addElement('.')
	root.addElement('b', True)
	root.addElement('.')
	root.addElement('b', True)
	root.addElement('*')
	root.addElement('a', True)
	root.addElement('|')
	root.addElement('b', True)
	root.addElement('a')

	root.addNumbers()
	root.firstPos()
	root.lastPos()
	root.print_tree()


def main(argv):
	if(len(sys.argv) != 1):
		sys.exit('Usage: Problema3.py <alphabet> <expession>')

	#strAlphabet=str(sys.argv[1])
	#arrAlphabet=parseAlphabet(strAlphabet)
	#a ='((a|b)*abb)'

	'''strExpression = str(sys.argv[2])
	if checkExpression(strExpression, arrAlphabet):
		strExpression += '#'
	else:
		sys.exit('Invalid expression for '+strAlphabet+' alphabet')'''
	buildTree()
	print arrPrintElements
	print arrNumbers

if __name__ == "__main__":
	main(sys.argv[1:])

	


#readAlphabet();