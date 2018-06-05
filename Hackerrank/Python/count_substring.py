def count_substring(string,sub_string):
	sub_string_length = len(sub_string)
	string_length = len(string)
	count = 0
	j = 0
	for i in range(string_length):
		j = i + sub_string_length
		if j > string_length :
			continue

		if string.find(sub_string,i,j)+1 :
			count = count + 1

	return(count)

string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
print(count)