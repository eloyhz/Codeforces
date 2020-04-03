# https://codeforces.com/problemset/problem/705/A
n = int(input())
print("I hate", end=' ')
for i in range(2, n + 1):
	print("that I", end=' ')
	if i & 1 == 0:
		print("love", end=' ')
	else:
		print("hate", end=' ')
print("it")
