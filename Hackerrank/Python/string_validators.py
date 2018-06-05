s = input()
characters = list(s)
alphabets = 0
digit = 0
lowercase = 0
uppercase = 0
special = 0


for character in characters :
	if character.isalpha():
		alphabets = 1
	elif character.isdigit() :	
		digit = 1
	else :
		special = 1

	if character.islower():
		lowercase = 1

	elif character.isupper():
		uppercase = 1

#case 1 any alphanumeric characters

if alphabets or digit :
	print("True")
else :
	print("False")

#case 2 any alphatical characters

if alphabets :
	print("True")
else :
	print("False")

#case 3 any digits
if digit :
	print("True")
else : 
	print("False")

#case 4 any lowercase characters

if lowercase:
	print("True")
else :
	print("False")
#case 5 any uppercase characters	

if uppercase:
	print("True")
else : 
	print("False")
