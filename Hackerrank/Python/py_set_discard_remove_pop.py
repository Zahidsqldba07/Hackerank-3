n = int(input())
mySet = map(int,input().split())
mySet = set(mySet)
N = int(input())
commands = list()
attribute = int()
method = str()
for i in range(N):
	commands.append(input().split())
#print(commands)
for i in range(len(commands)) :
	if len(commands[i]) == 2 :
		method = commands[i][0]
		attribute = int(commands[i][1])
		getattr(mySet,method)(attribute)
		#print(mySet)
	elif len(commands[i]) == 1 :
		method = commands[i][0]
		getattr(mySet,method)()
		#print(mySet)

print(sum(mySet))