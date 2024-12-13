from collections import Counter

from tqdm import tqdm

SAMPLE_INPUT = "sample_input.txt"
INPUT = "input.txt"

def stone_splitter(stoneVal, splits_dict):
    if stoneVal in splits_dict:
        return splits_dict[stoneVal]
    if stoneVal == "0":
        splits_dict[stoneVal] = "1"
        return "1"
    if len(stoneVal) % 2 == 0:
        half_len = int(len(stoneVal) / 2)
        a = stoneVal[:half_len].lstrip("0") or "0"
        b = stoneVal[half_len:].lstrip("0") or "0"
        splits_dict[stoneVal] = (a, b)
        return a, b
    splits_dict[stoneVal] = f"{int(stoneVal) * 2024}"
    return f"{int(stoneVal) * 2024}"

def process_stones(input_file, iterations=10_000):
    with open(input_file, "r") as f:
        allStones = f.read().strip().split()

    stone_counter = Counter(allStones)
    splits_dict = {}

    for i in tqdm(range(0, iterations)):
        unique_stones = list(stone_counter.keys())
        new_counter = Counter()
        for stone in unique_stones:
            split_result = stone_splitter(stone, splits_dict)
            if isinstance(split_result, tuple):
                for x in split_result:
                    new_counter[x] += stone_counter[stone]
            else:
                new_counter[split_result] += stone_counter[stone]
        stone_counter = new_counter
        print(f"After {i + 1} iterations: {sum(stone_counter.values())}")

process_stones(INPUT)