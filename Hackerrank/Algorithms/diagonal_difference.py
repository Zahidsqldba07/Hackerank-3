n = int(input().strip())
a = []
for i in range(n):
	temp = list(map(int,input().split()))
	a.append(temp)

def diagonalDifference(a):
	d1 , d2 = 0, 0
	for i in range(n):
		for j in range(n):
			if i == j :
				d1 = d1 + a[i][j]

	for i in range(n):
		for j in range(n):
			if i + j == (n-1) :
				d2 = d2 + a[i][j]

	dd = d1 - d2 
	if dd < 0 :
		dd = dd*(-1)
	return(dd)

print(diagonalDifference(a))