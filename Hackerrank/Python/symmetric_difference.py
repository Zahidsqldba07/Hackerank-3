M = int(input())
array_M = map(int,input().split())

N = int(input())
array_N = map(int,input().split())

def symmetric_difference(array_N,array_M):
	array_N = set(array_N)
	array_M = set(array_M)

	symmetric_difference1 = array_M.difference(array_N)
	symmetric_difference2 = array_N.difference(array_M)
	symmetric_difference1 = list(symmetric_difference1)
	symmetric_difference2 = list(symmetric_difference2)
	symmetric_difference = symmetric_difference1 + symmetric_difference2
	symmetric_difference = sorted(symmetric_difference)
	for i in symmetric_difference:
		print(i)

symmetric_difference(array_N,array_M)
