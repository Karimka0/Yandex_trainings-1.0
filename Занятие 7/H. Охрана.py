def proverka(list, n):
    guards = []
    guards_now = 0
    g_n = []
    for j in range(len(list)):
        if list[j][1] == 1:
            guards_now += 1
            g_n.append(list[j][2])
        elif list[j][1] == -1:
            guards_now -= 1
            g_n.remove(list[j][2])
        if guards_now == 0 and list[j][0] != 10000:
            return "Wrong Answer"
        elif guards_now == 1 and g_n[0] not in guards:
            guards.append(g_n[0])
    if len(guards) == n:
        return "Accepted"
    else:
        return "Wrong Answer"


k = int(input())
for i in range(k):
    a = list(map(int, input().split()))
    n = a[0]
    events = []
    k = 1
    for j in range(1, len(a), 2):
        events.append((a[j], 1, k))
        events.append((a[j+1], -1, k))
        k += 1
    events.sort()
    print(proverka(events, n))
