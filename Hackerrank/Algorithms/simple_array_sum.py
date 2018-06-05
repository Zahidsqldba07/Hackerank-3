def simpleArraySum(n,ar):
	mysum = 0
	for i in range(n):
		mysum = mysum + ar[i]
	return(mysum)


n = int(input().strip())
ar = list(map(int, input().split(' ')))
result = simpleArraySum(n,ar)
print(result)