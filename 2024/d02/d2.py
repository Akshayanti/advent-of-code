INPUT_FILE = "input.txt"

part1_total = 0
part2_total = 0

def part1(input_nums):
    if input_nums != sorted(input_nums) and input_nums != sorted(input_nums, reverse=True):
        return 0
    for i in range(len(input_nums) - 1):
        if abs(input_nums[i] - input_nums[i + 1]) not in [1, 2, 3]:
            return 0
    return 1

def part2(input_nums):
    if part1(input_nums) == 1:
        return 1
    if any([part1(num2) == 1 for num2 in [input_nums[:i] + input_nums[i + 1:] for i in range(len(input_nums))]]):
        return 1
    return 0

with open(INPUT_FILE) as f:
    for line in f:
        nums = list(map(int, line.strip().split()))
        part1_total += part1(nums)
        part2_total += part2(nums)

print(part1_total)
print(part2_total)