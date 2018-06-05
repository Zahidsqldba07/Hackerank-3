N,X = map(int,input().split())
data = list()
for i in range(X):
	data.append(list(map(float,input().split())))
x = [data[0]] + [data[1]] + [data[2]]
avg = 0
for i in range(N):
	avg = sum(list(zip(*x))[i])
	avg = avg/X
	a = '%.1f' %(avg)
	print(a)
#	print(avg)

#print(list(zip(*x)))