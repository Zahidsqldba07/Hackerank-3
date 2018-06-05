from collections import Counter
no_of_shoes = int(input())
available_shoes = list(map(int,input().split()))
available_shoes = Counter(available_shoes)
#print(available_shoes)
customers = int(input())
income = 0
for i in range(customers):
	size , price = map(int,input().split())
	if available_shoes[size] == 0:
		continue
	else :
		available_shoes[size] = available_shoes[size] - 1
		income = income + price
print(income)