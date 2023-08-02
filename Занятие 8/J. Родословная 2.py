def height(man):
    if man not in tree:
        return 0
    else:
        return 1 + height(tree[man])


N = int(input())
tree = {}
peoples = []
for i in range(N-1):
    child, parent = input().split()
    if parent not in peoples:
        peoples.append(parent)
    if child not in peoples:
        peoples.append(child)
    tree[child] = parent
peoples.sort()
for people in peoples:
    print(people, height(people))
