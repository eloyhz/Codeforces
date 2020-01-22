# Python3
# https://codeforces.com/contest/1294/problem/C

if __name__ == '__main__':
	t = int(input())
	for x in range(t):
		# print("Case", x + 1)
		n = int(input())
		i = 2
		div = []
		while n >= i and n > 1 and len(div) < 3:
			if n % i == 0:
				n = n // i
				div.append(str(i))
			i += 1
		if n == 1 and len(div) == 3:
			print("YES")
			print(' '.join(div), '')
		else:
			print("NO")
