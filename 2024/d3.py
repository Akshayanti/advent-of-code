import re

input_file = "input.txt"
# part1
with open(input_file, "r") as f:
    text = f.read()
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, text)
    numbers = [re.findall(r'\d{1,3}', match) for match in matches]
    part1 = 0
    for nums in numbers:
        part1 += int(nums[0]) * int(nums[1])
    print(f"Part1: {part1}")


# part2
with open(input_file, "r") as f:
    text = f.read()
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, text)
    updated_matches = []
    add_flag = True
    for x in matches:
        if x == "don't()":
            add_flag = False
        elif x == "do()":
            add_flag = True
        else:
            if add_flag:
                updated_matches.append(x)
    mul_numbers = [re.findall(r'\d{1,3}', match) for match in updated_matches if match.startswith("mul")]
    part2 = 0
    for nums in mul_numbers:
        part2 += int(nums[0]) * int(nums[1])
    print(f"Part2: {part2}")
