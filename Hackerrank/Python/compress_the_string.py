import itertools
S = input()
compression = list()
for group,items in itertools.groupby(S) :
	compression.append((len(list(items)) , int(group)))
print(*compression)