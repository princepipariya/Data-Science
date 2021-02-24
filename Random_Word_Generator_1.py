import random 
 
word_list = [	'Facetious', 'Doctrinaire', 'Didactic', 'Opprobrium', 'Avarice', 
				'Heretical', 'Empirical', 'Reconvene', 'Rebound', 'Abrogate', 
				'Staid', 'Eclectic', 'Bedraggled', 'Morose', 'Chary', 
				'Contrite', 'Detestable', 'Feign', 'Ingratiate', 'Complaisance', 
				'Retreat', 'Plodding', 'Potpourri', 'Exiguous', 'Surfeit', 
				'Fortuious', 'Vista', 'Bloster', 'Pedantic', 'Occlude', 
				'Lambast', 'Inchoate', 'Exscind', 'Descant', 'Refulgent', 
				'Sojourn', 'Infelicitous', 'Precursor', 'Guileless', 'Liturgy'
			] 

while True :
	repet = input('Press Y, y or ' ' for New Word: ')
	random_word = random.choice(word_list)
	if repet == 'y' or repet == 'Y' or repet == '' :	
		print(random_word)
		answer = input('Do you wanna see the answer?')
		if answer == 'y' or answer == 'Y' or answer == '' :
			i = 0
			for x in word_list:
				i = i + 1
				if x == random_word:
					print(i)
					break;
			print('\n') 
		else :
			print('Good!')
			print('\n')
	else :
		print('Thank You!')
		print('\n')
		exit()