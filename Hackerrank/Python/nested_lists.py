N = int(input())
main_list = list()
element_list = list()
flag = 0

def findSecondLast(seq):
	test = list()
	for i in range(len(seq)):
		test.append(seq[i][1])
	marks = dict()
	for i in test:
		marks[i] = marks.get(i,0) + 1
	lst = sorted(marks.items())
	secondLast = lst[1][0]
	return(secondLast)



for i in range(2*N) :
	flag = flag + 1
	element = input()
	if flag%2 == 0 :
		element = float(element)                        #because the second element is float
	element_list.append(element)
	
	if flag%2 != 0 :
		continue
	main_list.append(element_list)
	element_list = list()                                      #to reset the element list
#print(main_list)

#print(findSecondLast(main_list))
secondLast = findSecondLast(main_list)
secondLastNameList = list()
for i in range(len(main_list)):
	if main_list[i][1] == secondLast :
		secondLastNameList.append(main_list[i][0])

secondLastNameList = sorted(secondLastNameList)

for secondLastName in secondLastNameList :
	print(secondLastName)