from utils.utils import MatrixOperations
from functools import reduce

SAMPLE_INPUT = "sample_input.txt"
INPUT = "input.txt"

all_eqns = dict()

with open(INPUT, "r") as f:
    for line in f:
        val = line.strip().split(": ")[0]
        reqs = line.strip().split(": ")[1].split()
        all_eqns[int(val)] = [int(x) for x in reqs]

def is_acceptable_pt1(key, val):
    if not val:
        return False

    results = [val[0]]
    for val in val[1:]:
        new_res = []
        for res in results:
            new_res.append(res+val)
            new_res.append(res*val)
        results = new_res
    return key in results

p1_keys = [k for k, v in all_eqns.items() if is_acceptable_pt1(k, v)]
print(f"Part1: {sum(p1_keys)}")


def is_acceptable_pt2(key, val):
    if not val:
        return False

    results = [val[0]]
    for val in val[1:]:
        new_res = []
        for res in results:
            new_res.append(res+val)
            new_res.append(res*val)
            new_res.append(int(f"{res}{val}"))
        results = new_res
    return key in results


p2_keys = [k for k, v in all_eqns.items() if is_acceptable_pt2(k, v)]
print(f"Part2: {sum(p2_keys)}")