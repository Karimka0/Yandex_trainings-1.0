a = int(input())
b = int(input())
c = int(input())
left, right = 0, a + b + c
while right > left:
    m = (left+right) // 2
    if (4*a + 6*b + 8*c + 10*m) >= 7 * (a+b+c+m):
        right = m
    else:
        left = m + 1
print(left)
