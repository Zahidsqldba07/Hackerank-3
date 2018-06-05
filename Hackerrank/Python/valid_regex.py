import re
T = int(input())
for i in range(T):
	S = input()
	ans = re.compile(S)
	print(ans)