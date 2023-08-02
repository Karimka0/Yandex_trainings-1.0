n = int(input())
s1 = {}
s2 = {}
for i in range(n):
    a, b = input().split()
    s1[a] = b
    s2[b] = a
slovo = input()
if slovo in s1:
    print(s1[slovo])
else:
    print(s2[slovo])
