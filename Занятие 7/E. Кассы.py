n = int(input())
t = []
box_now = 0
for i in range(n):
    h1, m1, h2, m2 = map(int, input().split())
    if h1 * 60 + m1 == h2 * 60 + m2:
        box_now += 1
    elif h1 * 60 + m1 > h2 * 60 + m2:
        box_now += 1
        t.append((h1*60+m1, -1))
        t.append((h2*60+m2, 1))
    else:
        t.append((h1 * 60 + m1, -1))
        t.append((h2*60 + m2, 1))
t1, t_ans = 0, 0
t.sort()
for i in range(len(t)):
    if t[i][-1] == -1:
        box_now += 1
    elif t[i][-1] == 1:
        if box_now == n:
            t_ans += t[i][0] - t1
        box_now -= 1
    if box_now == n:
        t1 = t[i][0]
if box_now == n:
    t_ans += 1440 - t1
if len(t) == 0:
    t_ans = 1440
print(t_ans)
