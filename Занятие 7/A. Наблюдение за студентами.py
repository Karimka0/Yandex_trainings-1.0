n, m = map(int, input().split())
parts = []
for i in range(m):
    b, e = map(int, input().split())
    parts.append([b-1, -1])
    parts.append([e, 1])
parts.sort()
online = 0
ans = 0
for i in range(len(parts)):
    if online > 0:
        ans += parts[i][0] - parts[i-1][0]
    if parts[i][1] == -1:
        online += 1
    else:
        online -= 1
print(n-ans)
