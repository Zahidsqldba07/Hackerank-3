from collections import OrderedDict
characters_dict = OrderedDict()

S = list(input().rstrip())
#S = list(S)

for i in S:
	characters_dict[i] = characters_dict.get(i,0) + 1
temp_list = list()
new_tup = tuple()
for k,v in characters_dict.items():
	new_tup = (v,k)
	temp_list.append(new_tup)

temp_list = sorted(temp_list,reverse=True)[:3]
solution_list_reversed = temp_list
print(solution_list_reversed)

solution_list = list()
for v , k in temp_list:
	new_tup = (k,v)
	solution_list.append(new_tup)


print(solution_list)

k1 , k2 , k3 = temp_list[0][1] , temp_list[1][1] , temp_list[2][1]           #a b c etc.
v1 , v2 , v3 = temp_list[0][0] , temp_list[1][0] , temp_list[2][0]			#numbers

final_solution_list = list()

if v1 == v2 == v3 :
	final_solution_list = sorted(solution_list)

temp_list = list()
elif v1 == v2 :
	if v1 > v3 :
		temp_list = [(v1)]


print(final_solution_list)