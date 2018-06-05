N = int(input())
main_list = list()
elements_list = list()
new_elements_list = list()
database = dict()

for n in range(N) :
	elements = input().split()
	flag = 0
	for element in elements :
		flag = flag + 1 
		if flag == 1 :
			new_elements_list.append(element)
			continue
		element = float(element)
		new_elements_list.append(element)
	main_list.append(new_elements_list)
	new_elements_list = list()

for element in main_list:
	database[element[0]] = element[1],element[2],element[3]

find = input()
percentage = float()
percentage = sum(database[find])/3
a = "%.2f" %(percentage)
print(a)