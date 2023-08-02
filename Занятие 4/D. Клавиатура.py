n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))
for q in p:
    c[q-1] -= 1
for i in c:
    if i < 0:
        print("YES")
    else:
        print("NO")
