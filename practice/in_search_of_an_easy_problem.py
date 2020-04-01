# https://codeforces.com/problemset/problem/1030/A
n = int(input())
people = map(int, input().split())
is_hard = False
for p in people:
	if p == 1:
		is_hard = True
		break
if is_hard:
	print("hard")
else:
	print("easy")

