# https://codeforces.com/contest/1343/problem/A
t = int(input())
for _ in range(t):
	n = int(input())
	k = 2
	while True:
		d = (1 << k) - 1
		if n % d == 0:
			x = n // d
			print(x)
			break
		k += 1

	
