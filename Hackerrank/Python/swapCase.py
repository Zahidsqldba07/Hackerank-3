def swap_case(s):
	sentence = list(s)
	new_sentence = list()
	final_sentence = str()
	for letter in sentence :
		if letter.islower() :
			letter = letter.upper()
			new_sentence.append(letter)
			
			#print(letter)

		elif letter.isupper() :
			letter = letter.lower()
			new_sentence.append(letter)
			#print(letter)
		else :
			#print(letter)
			new_sentence.append(letter)
			continue

	for i in range(len(new_sentence)): 
		final_sentence = final_sentence + new_sentence[i] 
	return(final_sentence)


swap_case('HackerRank.com presents "Pythonist 2".')