n = int(input())
myList = list()
commands = list()
for i in range(n):
	commands.append(list(input().split()))
methods = list()
attributes = list()
for i in range(len(commands)):
	methods.append(commands[i][0])
	attributes.append(commands[i][1:])
#print(attributes)
formatted_attributes = list()
for i in range(len(attributes)):
	if len(attributes[i]) == 0 :
		formatted_attributes.append(None)
	else :
		for j in range(len(attributes[i])):
			formatted_attributes.append(int(attributes[i][j]))
#print(formatted_attributes)
for i in range(n):
	for j in range(len(attributes[i])):
		getattr(myList,methods[i])(tuple(attributes[i][:]))

