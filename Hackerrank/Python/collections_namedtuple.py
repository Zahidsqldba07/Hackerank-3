from collections import namedtuple
N = int(input())
spreadsheet = namedtuple('spreadsheet',','.join(input().split()))
avg = 0
for i in range(N):
	field1,field2,field3,field4 = input().split()
	newsheet = spreadsheet(field1,field2,field3,field4)
	avg = int(newsheet.MARKS) + avg
avg = float(avg/N)
print('%.2f' %(avg))