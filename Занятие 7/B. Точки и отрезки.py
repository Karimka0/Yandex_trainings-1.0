n, m = map(int, input().split())
events = []
for i in range(n):
    a, b = map(int, input().split())
    events.append((min(a, b), -1))
    events.append((max(a, b), 1))
M = list(map(int, input().split()))
for x in range(m):
    events.append((M[x], 0, x))
events.sort()
otr_now = 0
ans = [0] * m
for i in range(len(events)):
    if events[i][1] == -1:
        otr_now += 1
    elif events[i][1] == 0:
        ans[events[i][2]] = otr_now
    elif events[i][1] == 1:
        otr_now -= 1
print(*ans)
