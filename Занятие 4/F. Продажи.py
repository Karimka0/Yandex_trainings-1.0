dict = {}
a = open('input.txt', 'r')
for line in a:
    name, product, cost = line.split()
    cost = int(cost)
    if name not in dict:
        dict[name] = {product: cost}
    else:
        if product not in dict[name]:
            dict[name][product] = cost
        else:
            dict[name][product] += cost
for name in sorted(dict):
    print(f"{name}:")
    for tovar in sorted(dict[name]):
        print(tovar, dict[name][tovar])
