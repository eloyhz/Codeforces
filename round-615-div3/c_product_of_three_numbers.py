# Python3
# https://codeforces.com/contest/1294/problem/C

if __name__ == '__main__':
	t = int(input())
	for x in range(t):
		# print("Case", x + 1)
		n = int(input())
		nn = n
		i = 2
		div = []
		while n >= i and len(div) < 2:
			if n % i == 0:
				n = n // i
				div.append(i)
			i += 1
		if len(div) == 2:
			a = div[0]
			b = div[1]
			if nn % (a * b) != 0:
				print("NO")
			else:
				c = nn // (a * b)
				if c <= b:
					print("NO")
				else:
					print("YES")
					print(a, b, c, '')
		else:
			print("NO")
