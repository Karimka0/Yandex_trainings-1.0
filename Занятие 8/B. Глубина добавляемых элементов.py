def add(bin_tree, element):
    if element == bin_tree[0]:
        return
    elif element < bin_tree[0]:
        if bin_tree[1] == -1:
            bin_tree[1] = [element, -1, -1]
        else:
            add(bin_tree[1], element)
    else:
        if bin_tree[2] == -1:
            bin_tree[2] = [element, -1, -1]
        else:
            add(bin_tree[2], element)


def height_el(tree, element):
    if tree[0] == element:
        return 1
    elif element > tree[0]:
        return 1 + height_el(tree[2], element)
    else:
        return 1 + height_el(tree[1], element)


L = list(map(int, input().split()))
L1 = L[:-1]
bintree = [L1[0], -1, -1]
for i in range(1, len(L1)):
    add(bintree, L1[i])
ans = []
set1 = set()
for i in range(len(L1)):
    if L1[i] not in set1:
        set1.add(L1[i])
        ans.append(height_el(bintree, L1[i]))
print(*ans)
