from itertools import combinations_with_replacement
line = input().split()
S = line[0]
k = int(line[1])
c = list(combinations_with_replacement(sorted(S),k))
a = list()
for C in c :
	a.append(''.join(C))
for i in a:
	print(i)















	##########just edited the itertools_combinations.py file