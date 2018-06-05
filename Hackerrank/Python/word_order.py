from collections import OrderedDict
n = int(input())
word_dict = OrderedDict()
for i in range(n):
	word = input().rstrip()

	word_dict[word] = word_dict.get(word,0) + 1
print(len(word_dict.items()))
print(*word_dict.values())	