import itertools
def f(x):
	x = int(x)
	return(x*x)

K,M = map(int,input().split())
lists_k = list()
S = 0
for i in range(K):
	lists_k.append(sorted(list(map(int,input().split()))))
lists_k_final = list()
for i in range(K):
	lists_k_final.append(lists_k[i][1:])

# till now we've created a list of elements without the main size

all_cartesian_products = list(itertools.product(*lists_k_final))
#print(all_cartesian_products)
Sum = list()
for i in range(len(all_cartesian_products)) :
	for j in range(K):
		S = S + f(all_cartesian_products[i][j])
	Sum.append(S)
	S = 0
answer = list()
for i in range(len(Sum)):
	answer.append(Sum[i]%M)

answer = sorted(answer)
print(answer[len(answer)-1])