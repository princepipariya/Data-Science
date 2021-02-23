import random 
 
word_list = [	'1.) Filibuster', '2.) Inured', '3.) Tenuous', '4.) Precipitate', '5.) Martial', 
				'6.) Machinist', '7.) Pristine', '8.) Feckless', '9.) Tenacity', '10.) Perfunctory', 
				'11.) Ossified', '12.) Impersonate', '13.) Superfluous', '14.) Parody', '15.) Belie', 
				'16.) Rescind', '17.) Obstensible', '18.) Sibilint', '19.) Qualm', '20.) Perfidy', 
				'21.) Repudiate', '22.) Consternated', '23.) Exculpate', '24.) Arduous', '25.) Stupefy', 
				'26.) Blase', '27.) Alacrity', '28.) Approbation', '29.) Axiom', '30.) Canon', 
				'31.) Capricious', '32.) Convoluted', '33.) Disabuse', '34.) Effrontery', '35.) Exigent', 
				'36.) Fluminate', '37.) Irascible', '38.) Prattle', '39.) Prevaricate', '40.) Predilection', 
				'41.) Recant', '42.) Relagate', '43.) Sordid', '44.) Squander', '45.) Stymie',
				'46.) Tortuous', '47.) Trruculent', '48.) Veracity', '49.) Virulent', '50.) Paean', 
			] 

while True :
	repet = input('Press Y, y or ' ' for New Word: ')
	if repet == 'y' or repet == 'Y' or repet == '' :	
		random_word = random.choice(word_list) 
		print(random_word)
		print('\n')
	else :
		print('Thank You!')
		print('\n')
		exit()