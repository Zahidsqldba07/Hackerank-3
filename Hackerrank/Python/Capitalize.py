def capitalize(string) :
	fullName = string 
	result = list()
	fullName = fullName.split(" ")     #editable
	for parts in fullName:
		parts = parts.capitalize()
		result.append(parts)
	result=  " ".join(result)
	return(result)


string = input()
capitalized_string = capitalize(string)
print(capitalized_string)
