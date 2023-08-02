dict = {}
a = open('input.txt', 'r')
for line in a:
    p = line.split()
    if p[0] == "DEPOSIT":
        if p[1] not in dict:
            dict[p[1]] = int(p[2])
        else:
            dict[p[1]] += int(p[2])
    elif p[0] == "WITHDRAW":
        if p[1] not in dict:
            dict[p[1]] = -int(p[2])
        else:
            dict[p[1]] -= int(p[2])
    elif p[0] == "BALANCE":
        if p[1] not in dict:
            print("ERROR")
        else:
            print(dict[p[1]])
    elif p[0] == "TRANSFER":
        name1, name2, cost = p[1], p[2], int(p[3])
        if name1 not in dict:
            dict[name1] = -cost
        else:
            dict[name1] -= cost
        if name2 not in dict:
            dict[name2] = +cost
        else:
            dict[name2] += cost
    elif p[0] == "INCOME":
        for i in dict:
            if dict[i] > 0:
                dict[i] += int(p[1]) * dict[i] // 100
