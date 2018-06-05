def print_formatted(number):
	def binary(x):
		binary = bin(x) 
		binary = binary[2:]
		return(binary)
	def octal(x):
		octal = oct(x)
		octal = octal[2:]
		return(octal)
	def hexadecimal(x):
		hexadecimal = hex(x)
		hexadecimal = hexadecimal[2:]
		hexadecimal_prime = str()
		for i in list(hexadecimal):
			if i.isdigit():
				hexadecimal_prime = hexadecimal_prime + i 	
				continue
			else :
				i = i.capitalize()
				hexadecimal_prime = hexadecimal_prime + i
		return(hexadecimal_prime)

	width = len(list(binary(number)))
	n = number
	n = str()
	for i in range(1,number+1):
		c = str(i)
		formatted_decimal = c.rjust(width)
		formatted_octal = octal(i).rjust(width)
		formatted_hexadecimal = hexadecimal(i).rjust(width)   
		formatted_binary = binary(i).rjust(width)

		print(''.join(formatted_decimal+' ' +formatted_octal+ ' ' + formatted_hexadecimal+ ' ' +formatted_binary))


n = int(input())
print_formatted(n)