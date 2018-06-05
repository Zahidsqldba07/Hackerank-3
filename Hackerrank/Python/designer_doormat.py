N , M = map(int , input().split()) ; pattern = list() ; welcome = 'WELCOME'.center(M,'-')
for i in range(N//2):
	pattern.append(('.|.'*(2*i+1)).center(M,'-'))
print('\n'.join(pattern + [welcome] + pattern[::-1]))