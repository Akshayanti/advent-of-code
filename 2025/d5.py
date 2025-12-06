import sys

from tqdm import tqdm

filename="input.txt"

rs = []
cands = set()
with open(filename, 'r') as f:
    for line in tqdm(f):
        if "-" in line:
            low, high = map(int, line.strip().split("-"))
            rs.append((low, high-low))
        elif line == "\n":
            continue
        else:
            cand = int(line.strip())
            cands.add(cand)

cands = sorted(list(cands))


p1 = 0
def find_nearest_low(n):
    diff = sys.maxsize
    lowest = -1
    for i, _ in rs:
        if i > n:
            continue
        if min(n-i, diff) < diff:
            diff = min(diff, n-i)
            lowest = i
    if lowest == -1:
        return None
    return lowest

for x in tqdm(cands):
    nn = find_nearest_low(x)
    if nn is None:
        continue
    if any([x - z[0] <= z[1] for z in rs if z[0] <= nn]):
        p1 += 1

print(f"Part1: {p1}")

rs = [(low, low + diff) for low, diff in rs]
rs.sort()

merged = []
curr_low, curr_high = rs[0]

for low, high in rs[1:]:
    if low <= curr_high + 1:
        curr_high = max(curr_high, high)
    else:
        merged.append((curr_low, curr_high))
        curr_low, curr_high = low, high
merged.append((curr_low, curr_high))

p2 = 0
for low, high in merged:
    p2 += (high - low + 1)

print(f"Part2: {p2}")
print(len(merged))