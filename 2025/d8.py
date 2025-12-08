import sys

# filename = "sample.txt"
# max_count = 10
# total_count = 20

filename = "input.txt"
max_count = 1000
total_count = 1000

items = []

with open(filename) as f:
    for line in f:
        x, y, z = line.strip().split(",")
        items.append((int(x), int(y), int(z)))

def line_dist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2)

neigbors = {}
for x in items:
    for y in [z for z in items if z != x]:
        if (y, x) in neigbors:
            continue
        neigbors[(x, y)] = line_dist(x, y)

def sync(input_list):
    after = input_list
    before = []
    while before != after:
        before = after
        after = []
        for item in input_list:
            if after == []:
                after.append(item)
                continue
            unrolled_after = [x for y in after for x in y]
            if any([x in unrolled_after for x in item]):
                # find where to fit this item
                for x in after:
                    if any([y in x for y in item]):
                        x.update(item)
            else:
                after.append(item)
    return after

all_circuits = []
ix = 0

p1 = 1
for x1 in sorted(neigbors, key=lambda x: neigbors[x]):
    x, y = x1
    ns = set([x, y])
    added = False
    if all_circuits == []:
        all_circuits.append(ns)
        continue
    for i, z in enumerate(all_circuits):
        if x in z or y in z:
            all_circuits[i].add(x)
            all_circuits[i].add(y)
            added = True
            break
    if not added:
        if ns not in all_circuits:
            all_circuits.append(ns)
    all_circuits = sync(all_circuits)
    if ix == max_count-1:
        for x in sorted(all_circuits, key=lambda x: len(x), reverse=True)[:3]:
            p1 *= len(x)
        print(f"P1: {p1}")
    if len(all_circuits[0]) == max_count:
        print(f"P2: {x[0]*y[0]}, {ix-1}, {x}, {y}")
        exit(0)
    ix += 1