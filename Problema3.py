#3. Sa se scrie un program care primeste la intrare elementele 
#unei expresii regulate (alfabetul expresiei, expresia propriuzisa 
#(in forma prefixata sau infixata - adica forma naturala), care contine 
#3 tipuri de operatori: reuniune, concatenare si iteratie Kleene (*)). 
#Sa se determine un automat finit determinist (sa se afiseze elememtele 
#sale) care recunoaste acelasi limbaj ca cel descris de expresia regulata,
#folosind algoritmul de la curs.


#todo: beautify read text so that ' ' can be cleaned
def readAlphabet():
	isInputed = ''
	isInputed = raw_input('Please insert Alphabet (sigma):')
	if ',' in isInputed:
		isInputed = isInputed.split(',')
	print isInputed

#def readExpression():


readAlphabet();