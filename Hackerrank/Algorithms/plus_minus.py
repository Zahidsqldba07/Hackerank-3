n = int(input().strip())
arr = list(map(int,input().split()))

def plusMinus(arr):
	a, b, c= float(), float(), float()
	temp_a, temp_b, temp_c = 0, 0, 0
	for i in range(n):
		if arr[i] == 0 :
			temp_c += 1
		elif arr[i] < 0 :
			temp_b += 1
		else : 
			temp_a += 1 
	a, b, c = temp_a/n , temp_b/n , temp_c/n
	a = "{0:8.6f}".format(a)
	b = "{0:8.6f}".format(b)
	c = "{0:8.6f}".format(c)

	print(a)
	print(b)
	print(c)


plusMinus(arr)