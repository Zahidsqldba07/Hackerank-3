from collections import deque
N = int(input())
d = deque()
for i in range(N):
	line = input().split()
	methods = line[0]

	if len(line) == 1:
		attribute = None
		getattr(d,methods)()

	else :
		attribute = int(line[-1])
		getattr(d,methods)(attribute)

print(*d)