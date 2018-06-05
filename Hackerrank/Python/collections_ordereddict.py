from collections import OrderedDict 
N = int(input())
item_name_list = list()
net_price_list = list()

total_dictionary = OrderedDict()

for i in range(N):
	line = input().split()
	if len(line) == 3:
		item_name = ' '.join(line[:2])
		net_price = int(line[-1])

	elif len(line) == 2:
		item_name = line[0]
		net_price = int(line[-1])

	if item_name not in total_dictionary :
		total_dictionary[item_name] = net_price
		#print(total_dictionary)
	else :
		total_dictionary[item_name] = total_dictionary[item_name] + net_price

#print(total_dictionary)
for keys,values in total_dictionary.items():
	print(keys,values)

