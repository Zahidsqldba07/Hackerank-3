from itertools import combinations
line = input().split()
S = line[0]
k = int(line[1])
c = list()
for i in range(1,k+1):
	c = c + (list(combinations(sorted(S),i)))

a = list()
for C in c :
	a.append(''.join(C))
#a = sorted(a,key=str.upper)
for i in a:
	print(i)