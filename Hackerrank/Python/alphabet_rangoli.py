def print_rangoli(size):
	#let size = 5
	alphabets = 'abcdefghijklmnopqrstuvwxyz'
	subset = alphabets[:size]
	base = '-'.join(reversed(subset))     #making 
	rows = list()
		# Generate 
	'''--------e
       ------e-d
       ----e-d-c
       --e-d-c-b
       e-d-c-b-a'''

	for i in range(size-1,-1,-1):
		row = base[:len(base) - 2*i]
		row = '-'*(len(base)-len(row)) + row
		rows.append(row)

	#print(rows)
	uprows = rows
	downrows = list(reversed(uprows))
	leftHalf = uprows + downrows[1:]
	#print(downrows)
	#quarter = '\n'.join(rows)
	#print(quarter)
	half = '\n'.join(leftHalf)
	#print(leftHalf)
	full_rangoli = list()
	for i in range(len(leftHalf)) :
		new_row = leftHalf[i]
		rev_row = new_row[::-1]
		final_row = new_row + rev_row[1:]
		full_rangoli.append(final_row)

	full_rangoli = '\n'.join(full_rangoli)
	print(full_rangoli)





n = int(input())
print_rangoli(n)