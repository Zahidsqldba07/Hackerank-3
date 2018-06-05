a = list(map(int,input().split()))
b = list(map(int,input().split()))

def score(a,b):
	Alice = 0
	Bob = 0
	for i in range(3):
		if a[i] == b[i] :
			continue
		elif a[i] > b[i] :
			Alice += 1
		else :
			Bob += 1
	mystr = str(Alice)+' '+str(Bob)
	return(mystr)

print(score(a,b))