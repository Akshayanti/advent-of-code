filename="input.txt"

def find_largest_n_digit_num(n: int, l):
    new_num = 0
    start_idx = 0
    end_idx = len(l) - n + 1
    for i in range(n-1, -1, -1):
        z = max([x for x in l[start_idx:end_idx]])
        start_idx = l.find(z, start_idx, end_idx) + 1
        end_idx = len(l)+1 - i
        new_num = (new_num * 10) + int(z)
    return new_num


p1 = []
p2 = []
with open(filename, "r") as f:
    for line in f:
        l = line.strip()
        p1.append(find_largest_n_digit_num(2, l))
        p2.append(find_largest_n_digit_num(12, l))
    print(sum(p1), sum(p2))