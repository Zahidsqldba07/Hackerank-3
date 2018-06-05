from itertools import permutations
string = input().split()
S = string[0]
k = int(string[1])

P = list(permutations(S,k))
for p in P :
	print(''.join(p))