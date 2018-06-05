n = int(input())
A = set(map(int,input().split()))
N = int(input())
commands = list()
list_of_other_set = list()

for i in range(N):
	commands.append(input().split())
	list_of_other_set.append(set(map(int,input().split())))
#print(commands)
#print(list_of_other_set)
methods = str()
other_set = set()
for i in range(len(commands)):
	method = commands[i][0]
	other_set = list_of_other_set[i]
	getattr(A,method)(other_set)

print(sum(A))