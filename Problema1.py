'''1.Program care simuleaza modul de translatare al unei scheme de translatare 
orientata catre sintaxa (STOS).Programul citeste (dintr-un fisier sau de la consola)
elementele STOS oarecare. Programul permite citirea unui nr oarecare de siruri
peste alfabetul de intrare. Pentru fiecare astfel de sir de intrare se afiseaza 
toate iesirile (siruri peste alfabetul de iesire) corespunzatoare.'''

import sys

class Word(object):
	"""docstring for Word"""
	def __init__(self, w1, w2):
		super(Word, self).__init__()
		self.word1 = w1
		self.word2 = w2

class STOS(object):
	"""docstring for STOS"""
	def __init__(self, neterminale, input_alfabet, output_alfabet, start_symbol, rules):
		super(STOS, self).__init__()
		self.N = neterminale 
		self.Vi = input_alfabet
		self.Ve = output_alfabet
		self.S = start_symbol
		self.R = rules

	@staticmethod
	def find_first_pos(word, char):
		for i in range(len(word)):
			if char == word[i]:
				return i

	def insert_char_at_pos(char, pos, word):
		word = word[:pos] + word[:pos+1]
		word = word[:pos] + str(char) + word[pos:]
		return word

	def addToQueue(self, arrQueue, charToAdd):
		for i in range(self.R):
			if self.R[i][0] == charToAdd:
				arrQueue.append(self.R[i])
		return arrQueue

	#for all elemets in arrQueue and all elemets of arrWords 
	#apply rules from queue to elements that apply and delete them from queue
	#do stuff again to populate queue with elemets to apply to words array
	#print array of words.
	
	def emptyQueue(self, arrQueue, word):
		arrWords = []
		for queued in arrQueue: 
				#this calls first pos with the word and the start symbol and with this
				#calls insert_char_at_pos with the word and char to add.
				word1 = insert_char_at_pos(queued[1], find_first_pos(word[0], queued[0]), word[0])
				word2 = insert_char_at_pos(queued[2], find_first_pos(word[1], queued[0]), word[1])
				arrWords.append((word1, word2))
		return arrWords






	# primeste cuvantul
	# face in fct de reguli si aia e.
	def do_stuff(self, arrWords):
		arrRules = self.R
		arrQueue = []
		for word in arrWords:
			for i in range(len(word[0])):
				if word[i]=='S':
					self.addToQueue(arrQueue, 'S')
					alteredWords = self.emptyQueue(arrQueue, arrQueue, word)
					arrWords.append(alteredWords)
					#call function with updated word1
				if word1[i]=='A':
					self.addToQueue(arrQueue, 'A')
					#call function with updated word2

def parseString(string):
	return string.split(',')


# parseaza regulile in forma 
# [['S', 'aAbA', ' aAA'], ['S', 'bAaA', ' bAA'], ['A', 'aAbA', ' AA'], 
# ['A', 'bAaA', ' AA'], ['A', '^', ' ^']]

def parseRules(rules):
	inter=[]
	arrRules=[['' for x in range(3)] for x in range(len(rules))]
	counter=0	
	for i in range(len(rules)):
		rules[i]=rules[i].replace('\n', '')
		inter.append(rules[i].split('->'))
	for i in range(len(inter)):
		temp=inter[i][1].split(',')
		arrRules[i][0]=inter[i][0]
		arrRules[i][1]=temp[0]
		arrRules[i][2]=temp[1]
	return arrRules

def main():
	f=open('input.txt', 'rw')

	neterminale=f.readline()
	arrNeterminale=parseString(neterminale)

	input_alfabet=f.readline()
	arrInputAlfa=parseString(input_alfabet)

	output_alfabet=f.readline()
	arrOutputAlfa=parseString(output_alfabet)

	start_symbol=f.readline()

	#reading the no of rules
	ceva = f.readline()
	nRules= int(ceva)
	rules=[]
	for i in range(nRules):
		rules.append(f.readline())

	arrRules=parseRules(rules)
	print arrRules
	print 'P=('+str(arrNeterminale)+', '+str(arrInputAlfa)+', '+str(arrOutputAlfa)+', '+str(start_symbol)+', '+str(rules)+')'

	word  =f.readline()
	print word

	# do_stuff()



if __name__=="__main__":
	main()