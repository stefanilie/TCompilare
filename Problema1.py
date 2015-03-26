'''1.Program care simuleaza modul de translatare al unei scheme de translatare 
orientata catre sintaxa (STOS).Programul citeste (dintr-un fisier sau de la consola)
elementele STOS oarecare. Programul permite citirea unui nr oarecare de siruri
peste alfabetul de intrare. Pentru fiecare astfel de sir de intrare se afiseaza 
toate iesirile (siruri peste alfabetul de iesire) corespunzatoare.'''

import sys

def parseString(string):
	return string.split(',')

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

	'''
		TODO:
			- parse input from rules
			- ask for start symbol when entering
	'''
	ceva = f.readline()
	nRules= int(ceva)
	rules=[]
	for i in range(nRules):
		rules.append(f.readline())

	arrRules=parseRules(rules)
	#print 'P=('+str(arrNeterminale)+', '+str(arrInputAlfa)+', '+str(arrOutputAlfa)+', '+str(start_symbol)+', '+str(rules)+')'




if __name__=="__main__":
	main()