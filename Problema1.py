'''1.Program care simuleaza modul de translatare al unei scheme de translatare 
orientata catre sintaxa (STOS).Programul citeste (dintr-un fisier sau de la consola)
elementele STOS oarecare. Programul permite citirea unui nr oarecare de siruri
peste alfabetul de intrare. Pentru fiecare astfel de sir de intrare se afiseaza 
toate iesirile (siruri peste alfabetul de iesire) corespunzatoare.'''

import sys

def main():
	neterminale=str(input('Introduceti neterminalele: '))
	input_alfabet=str(input('Introduceti alfabetul de intrare: '))
	output_alfabet=str(input('Introduceti alfabetul de iesire: '))
	start_symbol=str(input('Introduceti simbolul de start: '))

	'''
		TODO:
			- parse input from rules
			- ask for start symbol when entering
	'''
	nRules=str(input('Introduceti numarul de reguli:'))
	rules=[]
	for i in range(nRules):
		rules.append(str(input('Introduceti regula cu numarul '+i+': ')))




if __name__="__main__":
	main()