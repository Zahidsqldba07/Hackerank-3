def minion_game(string):
	stuart_score = 0
	kevin_score = 0
	vowels = list("AEIOU")
	for i in range(len(string)):
		if string[i] in vowels :
			kevin_score = kevin_score + len(string) - i
		else :
			stuart_score = stuart_score + len(string) - i 

	if (kevin_score > stuart_score) :
		print("Kevin",kevin_score)
	elif (stuart_score == kevin_score) :
		print("Draw")

	else :
		print("Stuart",stuart_score)





s = input()
minion_game(s)