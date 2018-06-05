def split_and_join(line):
	words = line.split(" ")
	words = "-".join(words)
	return(words)
print(split_and_join("this is an input string"))