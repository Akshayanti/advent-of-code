from utils.utils import freq_analysis

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
print(total_sum)

# part2
total_sim = 0
freq_l2 = freq_analysis(l2)
for x in l1:
    if x not in l2:
        continue
    total_sim += freq_l2[x] * x
print(total_sim)
