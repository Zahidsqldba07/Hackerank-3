from collections import defaultdict
n , m = map(int,input().split())
A = defaultdict(list)
for a in range(n):
	wordA = input()
	A[wordA].append(a+1)

B = list()

for b in range(m):
	B.append(input())

for i in B:
	if i in A.keys():
		print(*A[i])
	else:
		print(-1)

