# https://codeforces.com/contest/1343/problem/B
t = int(input())
for _ in range(t):
	n = int(input())
	n //= 2
	if n % 2 == 1:
		print("NO")
		continue
	print("YES")
	for x in range(2, (n << 1) + 1, 2):
		print(x, end=" ")
	for x in range(1, (n << 1) - 1, 2):
		print(x, end=" ")
	print(x + 2 + n)
