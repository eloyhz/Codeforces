# Python3
# https://codeforces.com/contest/1294/problem/B

t = int(input())
for _ in range(t):
	n = int(input())
	packages = []
	for _ in range(n):
		xi, yi = map(int, input().split())
		packages.append((xi, yi))
	packages.sort()
	path = []
	r = (0, 0)
	valid_path = True
	while valid_path and len(packages) > 0:
		p = packages.pop(0)
		# first let's try to move over x
		x = p[0] - r[0]
		if x < 0:
			valid_path = False
			break
		for _ in range(x):
			path.append('R')
			r = (r[0] + 1, r[1])
		y = p[1] - r[1]
		if y < 0:
			valid_path = False
			break
		for _ in range(y):
			path.append('U')
			r = (r[0], r[1] + 1)

	if valid_path:
		print("YES")
		print(''.join(path))
	else:
		print("NO")

