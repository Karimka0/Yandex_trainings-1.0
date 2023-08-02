g, s = map(int, input().split())
w = sorted(input())
st = input()
k = 0
for i in range(len(st)-len(w)+1):
    if sorted(st[i:i+len(w)]) == w:
        k += 1
print(k)
