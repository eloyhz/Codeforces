# https://codeforces.com/problemset/problem/785/A
n = int(input())
s = 0
for _ in range (n):
	f = input()
	if f == "Tetrahedron":
		s += 4
	elif f == "Cube":
		s += 6
	elif f == "Octahedron":
		s += 8
	elif f == "Dodecahedron":
		s += 12
	elif f == "Icosahedron":
		s += 20
print(s)
