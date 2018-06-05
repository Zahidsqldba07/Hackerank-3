x = input().split()
n = int(x[0])
m = int(x[1])
array = list(map(int,input().split()))
set_A = set(map(int,input().split()))
set_B = set(map(int,input().split()))

#aInArray = set_A.intersection(array)
#bInArray = set_B.intersection(array)

#happiness = len(aInArray) - len(bInArray)
happiness = 0
for i in array:
	if i in set_A:
		happiness = happiness + 1 
	elif i in set_B :
		happiness = happiness - 1



print(happiness)

