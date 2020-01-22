t = int(input())
for _ in range(t):
	a, b, c, n = map(int, input().split())
	B = n + a - 2 * b + c
	if B % 3 != 0 or B < 0:
		print("NO")
		continue
	B = B // 3
	C = n + a + b - 2 * c
	if C % 3 != 0 or C < 0:
		print("NO")
		continue
	C = C // 3
	A = n - B - C
	if A < 0:
		print("NO")
		continue
	print("YES")
