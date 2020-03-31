# https://codeforces.com/problemset/problem/1328/A
t = int(input())
while t > 0:
	a, b = map(int, input().split())
	r = a % b
	if r == 0:
		print("0")
	else:
		r = b - r
		print(r)
	t -= 1
