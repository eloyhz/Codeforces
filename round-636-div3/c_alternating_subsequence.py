# https://codeforces.com/contest/1343/problem/C
t = int(input())
for _ in range(t):
	n = int(input())
	positive = []
	negative = []
	seq = []
	alt = 0
	for a in input().split():
		ai = int(a)
		if ai > 0:
			positive.append(ai)
			if alt == 0:
				alt = 1
			elif alt == -1:
				alt = 1
				seq.append(max(negative))
				negative = []
		else:
			negative.append(ai)
			if alt == 0:
				alt = -1
			elif alt == 1:
				alt = -1
				seq.append(max(positive))
				positive = []
	if alt == 1:
		seq.append(max(positive))
	elif alt == -1:
		seq.append(max(negative))
	print(sum(seq))

