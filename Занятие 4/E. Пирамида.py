n = int(input())
dict = {}
for i in range(n):
    w, h = map(int, input().split())
    if w not in dict:
        dict[w] = h
    else:
        if dict[w] < h:
            dict[w] = h
s = 0
for i in dict:
    s += dict[i]
print(s)
