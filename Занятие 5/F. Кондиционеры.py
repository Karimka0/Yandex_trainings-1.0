n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
ans = 0
kond = []
for i in range(m):
    b, c = map(int, input().split())
    kond.append([c, b])
kond.sort()
left = 0
for i in range(n):
    while kond[left][1] < a[i]:
        left += 1
    else:
        ans += kond[left][0]
print(ans)
