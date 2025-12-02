def part1(low: int, high: int) -> list:
    invalid_ids = []
    if len(str(low)) % 2 == 1:
        low = "1" + "0"*len(str(low))
        low = int(low)
    if len(str(high)) % 2 == 1:
        high = "9" * (len(str(high)) - 1)
        high = int(high)
    if low >= high:
        return []
    low_half = len(str(low)) // 2
    high_half = len(str(high)) // 2

    low_first_half = str(low)[:low_half]
    high_first_half = str(high)[:high_half]

    for i in range(int(low_first_half), int(high_first_half)+1):
        new_num = str(i)*2
        if low <= float(new_num) <= high:
            invalid_ids.append(int(new_num))
    return sorted(invalid_ids)

def part2(low: int, high: int) -> list:
    invalids = set()
    for cand in range(pow(10, 0), pow(10, 6)):
        i = len(str(cand))
        lower_count = len(str(low))//i
        high_count = len(str(high))//i
        if lower_count == 0 or high_count == 0:
            continue
        for x in range(lower_count, high_count+1):
            if x < 2:
                continue
            new_num = str(cand)*x
            if low <= int(new_num) <= high:
                invalids.add(int(new_num))
    return sorted(list(invalids))

def read_input():
    list_of_ranges = []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                continue
            else:
                line = line.strip()
                list_of_ranges += line.split(",")
    return list_of_ranges

total1 = 0
total2 = 0
for range_nums in read_input():
    print("RANGE:", range_nums)
    low, high = range_nums.split("-")
    invalids1 = part1(int(low), int(high))
    invalids2 = part2(int(low), int(high))
    print(len(invalids1), invalids1)
    print(len(invalids2), invalids2)
    total1 += sum(invalids1)
    total2 += sum(invalids2)
print(total1, total2)