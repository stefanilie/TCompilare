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
class Automata:
	bIsFinal=False
	arrFollowPos={}



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
		self.bIsVisited=False

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
				self.nCount=-counter
			print 'sunt in nodul '+self.strValue+' si am counter='+str(self.nCount)+' si left= '+str(self.left.strValue)+' si right='+str(self.right.strValue)
			self.right.addNumbers()

	def nullable(self, count):
		if self.nCount == count:
			if self.strValue=='^' or self.strValue=='*':
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

#returneaza array de array!!!!!!!!!!!!! vezi cum faci
#eventual bagi chestie cu return element cu element
	def firstPos(self, count):
		value=0
		print 'sunt in nodul '+str(self.strValue)+' cu indexul '+str(self.nCount)+' si count='+str(count)
		if self.nCount==count:
			print 'am intrat in self.nCount==count'
			if self.strValue=='^':
				print 'sunt pe ^'
				return None
			else: 
				#sigur aici e asa?
				print 'returneaza ncount=' +str(self.nCount)
				return self.nCount
		elif self.strValue=='|':
			if self.left.strValue!=None and self.right.strValue!=None:
				value=self.left.firstPos(count)
				print 'value=', value
				self.arrFirstPos.append(value)
				print self.arrFirstPos
				
				value=self.right.firstPos(count)
				self.arrFirstPos.append(value)

				self.arrFirstPos = [x for x in self.arrFirstPos if x is not None]
				return self.remove_duplicates(self.arrFirstPos)
		elif self.strValue=='.':
			#print '\tam itrat in pe al doilea else'
			if self.left.strValue!=None and self.right.strValue!=None:
				#print '\tstg si dr sunt dif de none'
				print '?'+str(self.left.nullable(self.left.nCount))
				if self.left.nullable(self.left.nCount):
					#print 'self.left.nullable(self.left.count) e true'
					value=self.left.firstPos(count)
					self.arrFirstPos.append(value)

					value=self.right.firstPos(count)
					self.arrFirstPos.append(value)
					
					return self.remove_duplicates(self.arrFirstPos)
				else:
					print 'sunt pe else de la nullable'
					return self.arrFirstPos.append(self.left.firstPos(count))
		elif self.strValue=='*':
			print str('am intrat in elif self.strValue==*:')
			if self.left.strValue!=None:
				print str('am intrat in if self.left.strValue!=None and self.right.strValue==None:')
				value=self.left.firstPos(count)
				self.arrFirstPos.append(value)
				
				return self.remove_duplicates(self.arrFirstPos)
			elif self.right.strValue!=None:
				print str('am intrat in elif self.left.strValue==None and self.right.strValue!=None:')
				value=self.right.firstPos(count)
				self.arrFirstPos.append(value)
				return self.remove_duplicates(self.arrFirstPos)

	def remove_duplicates(self, values):
		print values
		output = []
		seen = set()
		for value in values:
# If value has not been encountered yet,
# ... add it to both list and set.
			if value not in seen:
				output.append(value)
				seen.add(value)
		return output

	#todo: 'not in array' feature
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

	#verifica neaparat daca faci copierea cum trebuie din lastpos in firstpos
	def followPos(self, count):
		if self.left.strValue!=None:
			self.left.lastPos(self.left.nCount)
		if self.nCount==count and count!=0:
			return self.arrLastPos
		if self.strValue=='.' or self.strValue=='|':
				for i in range(len(self.left.arrLastPos)):
					for j in range(len(self.right.arrFirstPos)):
						set(self.arrFollowPos.extend(self.followPos(i)))
		if self.strValue=='*':
			if self.left.strValue!=None and self.right.strValue==None:
				for i in range(len(self.left.arrLastPos)):
					for j in range(len(self.left.arrFirstPos)):
						set(self.arrFollowPos.extend(self.followPos(i)))
			elif self.left.strValue==None and self.right.strValue!=None:
				for i in range(len(self.right.arrLastPos)):
					for j in range(len(self.right.arrFirstPos)):
						set(self.arrFollowPos.extend(self.followPos(i)))

	def printRoot(self):
		print 'This is the root: ', self.strValue

	def printFirstPos(self):
		if self.strValue!=None:
			self.left.printFirstPos()
			if self.left.strValue==None and self.right.strValue==None:
				print 'First pos pentru '+str(self.strValue)+ ' cu indexul '+str(self.nCount)+' este:'+ str(self.arrFirstPos)
			self.right.printFirstPos()

	def printLastPos(self):
		if self.strValue!=None:
			self.left.printLastPos()
			if self.left.strValue==None and self.right.strValue==None:
				print 'Last pos pentru'+str(self.strValue)+' este:'+ str(self.arrLastPos)
			self.right.printLastPos()

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

def isLetter(char):
	if char.isalpha():
		return True
	else:
		return False

#def buildTree(expression):
def buildTree():
#	for i in range(len(expression)-1):
#		if isLetter(expression[i]) and expression[i-1] in [')', *]

#a ='((a|b)*abb)'


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
	'''for i in range(1, 7, 1):
		root.firstPos(i)
	root.printFirstPos()

	for i in range(1, 7, 1):
		root.lastPos(i)
	root.printLastPos()'''
	root.firstPos(1)
	root.printFirstPos()
	return root

'''
tf = dict()
state_counter=0
dictStates={}

def createTransition(d, root):
    dictRoot={}
    #inversez keyul cu valueul ca sa pot sa accesez toate nodurile
    for k, v in d.items():
        dictRoot.setdefault(v, []).append(k)

    #creez tranzitiile
    for k, v in dictRoot.items():
        arrFollowPos=[]
        for i in range(len(v)):
            arrFollowPos=list(set(arrFollowPos.append(root.followPos(v[i]))))
        tf[(state_counter, k)] = arrFollowPos
        state_counter+=1
        dictStates.update({state_counter: arrFollowPos})
        createTransition(arrFollowPos)
        if k=='#':
            accept_states.append(arrFollowPos)  

states=[]
for i in range(state_counter):
    states.update(i)
alphabet=[]
alphabet = parseAlphabet(arrAlphabet)

'''

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
	root = buildTree()
	root.printRoot()


	#print arrPrintElements
	#print arrNumbers

if __name__ == "__main__":
	main(sys.argv[1:])

	


#readAlphabet();