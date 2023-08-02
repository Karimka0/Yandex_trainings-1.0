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


def sheets(tree, element):
    if element == tree[0]:
        if tree[1] == -1 and tree[2] == -1:
            return tree[0]
        else:
            return
    elif element < tree[0]:
        return sheets(tree[1], element)
    else:
        return sheets(tree[2], element)


L = list(map(int, input().split()))
L1 = L[:-1]
bintree = [L1[0], -1, -1]
for i in range(1, len(L1)):
    add(bintree, L1[i])
L2 = [i for i in set(L1)]
L2.sort()
for el in L2:
    if sheets(bintree, el) is not None:
        print(sheets(bintree, el))
