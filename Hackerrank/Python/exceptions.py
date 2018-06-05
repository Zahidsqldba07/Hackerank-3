T = int(input())
for i in range(T):
	a,b = map(str,input().split())
	div = 0
	try :
		print(int(a)//int(b))
	except Exception as e :
		print("Error Code:",e)
		