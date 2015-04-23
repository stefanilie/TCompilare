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

	#returns rule/rules that start with the first char of the word
	def search_rule_by_char(char):
		rules=[]
		for rule in self.R:
			if char == rule[1][0]:
				rules.append(rule)
		return rules

	#searches rules by nnonterminal.
	def search_rule_by_net(net):
		rules=[]
		for rule in self.R:
			if net == rule[0]:
				rules.append(rule)
		return rules

	#inserts rule at position, deleting the N that is found at that pos
	def insert_rule_at_pos(rule, word, pos):
		word = word[:pos] + word[pos+1:]
		word = word[:pos] + str(rule[1]) + word[pos:]
		return word

	#returns first pos of char found in word
	def find_first_pos(char, word):
		for i in range(len(word)):
			if word[i]==char:
				return i

	def check_lenght(self, word, possible):
		count=0
		ok=False
		for w in range(len(possible)):
			#daca litera e in alf de intrare, 
			if possible[w] in self.Vi:
				count+=1
			#daca e adevarat atunci inseamna ca possible contine litera mare
			if possible[w] in self.N:
				ok=True
		if count > len(word) or (count == len(word) and ok):
			return False
		else:
			return True

	def apply_rule(word, rules, word):
		for rule in rules:
			word = self.insert_rule_at_pos(rule, word, self.find_first_pos(rule[0], word))
			self.try_shit(word, rules, possible)

	def try_shit(self, word, possible):
		result_queue=[]
		if self.check_lenght(word, possible):
			
		if possible == '':
			rules = search_rule_by_char(word[0])
			self.apply_rule(word, rules, possible)
			#if rule is ok add to result by index of the rule list
		else:
			self.check_if_valid(word, possible) #TODO
		self.try_shit(word[1:], possible)


	def do_stuff(self, arrWords):
		arrRules = self.R
		arrQueue = []
		for word in arrWords:
			self.try_shit(word, '')
		return arrWords


def parseString(string):
	string = string.replace('\n', '')
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

# parses this "S, S"
# into this: [["S", "S"]]
def parseWords(words):
	arrWords=[]
	for i in range(len(words)):
		words[i] = words[i].replace('\n', '')
		arrWords.append(words[i].split(','))
	return arrWords

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
	#print arrRules
	#print 'P=('+str(arrNeterminale)+', '+str(arrInputAlfa)+', '+str(arrOutputAlfa)+', '+str(start_symbol)+', '+str(rules)+')'

	#reading the no of words
	ceva = f.readline()
	nWords= int(ceva)
	words=[]
	for i in range(nWords):
		words.append(f.readline())
	arrWords = parseWords(words)
	
	objStos = STOS(arrNeterminale, arrInputAlfa, arrOutputAlfa, start_symbol, arrRules)
	print "Za rezult!:"
	print objStos.do_stuff(arrWords)

	

	# do_stuff()



if __name__=="__main__":
	main()