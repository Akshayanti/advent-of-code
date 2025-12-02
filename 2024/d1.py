from collections import Counter

l1 = []
l2 = []

INPUT_FILE = "input.txt"


with open(INPUT_FILE) as f:
    for line in f:
        r1, r2 = line.strip().split()
        l1.append(int(r1))
        l2.append(int(r2))

# part1
total_sum = 0
for x, y in zip(sorted(l1), sorted(l2)):
    total_sum += abs(x - y)
print(f"Part1: {total_sum}")

# part2
freq_l2 = Counter(l2)
print(f"Part2: {sum([freq_l2[x]*x for x in l1])}")
