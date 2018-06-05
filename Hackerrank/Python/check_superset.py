A = set(map(int,input().split()))
n = int(input())
list_of_sets = list()
for i in range(n):
	list_of_sets.append(set(map(int,input().split())))
flag = 0
for i in list_of_sets:
	if A.intersection(i) != i :
		continue
	flag = flag + 1

if flag == len(list_of_sets):
	print('True')
else:
	print('False')

