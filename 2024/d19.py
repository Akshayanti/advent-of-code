from functools import lru_cache

avail_towels = []
towels_to_check = []
with open("input.txt") as f:
    for line in f:
        if line != "\n" and "," in line:
            avail_towels = [towel.strip() for towel in line.strip().split(",")]
        elif line != "\n":
            towels_to_check.append(line.strip())

@lru_cache(None)
def count_ways(target, word_bank):
    if target == "":
        return 1
    total_ways = 0
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            total_ways += count_ways(suffix, tuple(word_bank))
    return total_ways

part1 = 0
part2 = 0
for towel in towels_to_check:
    ways_to_construct = count_ways(towel, tuple(avail_towels))
    if ways_to_construct > 0:
        part2 += ways_to_construct
        part1 += 1
print(part1, part2)