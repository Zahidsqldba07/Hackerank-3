n = input()
n = int(n)
A_list = list()
A_list = input().split()
for i in range(len(A_list)):
	A_list[i] = int(A_list[i])

A_dict = dict()
for stuff in A_list :
	A_dict[stuff] = A_dict.get(stuff,0) + 1

A_tup_list = sorted(A_dict.items())
A_tup_list = sorted(A_tup_list,reverse=True)

x,y = A_tup_list[1]
print(x)