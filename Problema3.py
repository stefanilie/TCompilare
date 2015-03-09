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
class Tree:
	def __init__(self):
		self.left=None
		self.right=None
		self.strValue=None
		self.bNullable = None
		self.nCount =None
		self.arrChestii=None

	def __init__(self, regex):
		self.regex = regex
		self.left=None
		self.right=None
		self.strValue=None
		self.bNullable = None
		self.nCount =None
		self.arrChestii=None

	def addElement(self, value, bIsLettter=False, b):
		if self.strValue==None and self.left==None and self.right==None:
				self.strValue = value
				self.right = Tree()
				self.left = Tree()
		elif bIsLettter:
			self.right.addElement(value, true)
		elif not bIsLettter:
			self.left.addElement(value, false)

	def print_tree(self):
		if self.value!=None:
			self.left.print_tree()
			arrPrintElements.append(self.value)
			self.right.print_tree()
			

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

def buildTree(expression):
	root = Tree(expression)
		nPCounter=0
	for i in range(len(expression), -1, -1):
		if expression[i] == ')':
			nPCounter+=1
		elif expression[i] == '(':
			nPCounter-=1

		if expression[i] not in ['(', ')', '*', '|', '.', ' ']:
			if expression[i-1] not in ['(', ')', '*', '|', '.', ' ']:
				root.addElement('.')


def main(argv):
	if(len(sys.argv) != 3):
		sys.exit('Usage: Problema3.py <alphabet> <expession>')

	strAlphabet=str(sys.argv[1])
	arrAlphabet=parseAlphabet(strAlphabet)
	#a ='((a|b)*abb)'

	strExpression = str(sys.argv[2])
	if checkExpression(strExpression, arrAlphabet):
		strExpression += '#'
	else:
		sys.exit('Invalid expression for '+strAlphabet+' alphabet')
	#produce_tree(a)

if __name__ == "__main__":
	main(sys.argv[1:])

	


#readAlphabet();