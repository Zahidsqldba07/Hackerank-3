n = int(input())
input_line = input()
input_line = input_line.split()
for i in range(0,n) :
	input_line[i] = int(input_line[i])
t = tuple(input_line)
print(hash(t))