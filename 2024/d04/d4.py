import re
import itertools


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def check_row(matrix):
    total_count = 0
    for row in matrix:
        content = "".join(row)
        total_count += len(re.findall(r"XMAS", content))
        total_count += len(re.findall(r"SAMX", content))
    return total_count

def check_verticals(matrix):
    return check_row(transpose(matrix))

def check_diagonals(matrix):
    total_count = 0
    i_max = len(matrix)
    j_max = len(matrix[0])
    for i in range(i_max):
        for j in range(j_max):
            if matrix[i][j] != "X":
                continue
            if i + 3 < len(matrix):
                if j + 3 < len(matrix[0]):
                    content = "".join([matrix[i+k][j+k] for k in range(4)])
                    total_count += len(re.findall(r"XMAS", content))
                if 0 <= j - 3:
                    content = "".join([matrix[i+k][j-k] for k in range(4)])
                    total_count += len(re.findall(r"XMAS", content))
            if 0 <= i - 3:
                if j + 3 < len(matrix[0]):
                    content = "".join([matrix[i-k][j+k] for k in range(4)])
                    total_count += len(re.findall(r"XMAS", content))
                if 0 <= j - 3:
                    content = "".join([matrix[i-k][j-k] for k in range(4)])
                    total_count += len(re.findall(r"XMAS", content))
    return total_count


def generate_possibilities(original_string):
    replacement_chars = "XMAS"

    dot_indices = [i for i, char in enumerate(original_string) if char == '.']

    combinations = itertools.product(replacement_chars, repeat=len(dot_indices))

    possible_strings = []
    for combo in combinations:
        temp_list = list(original_string)
        for index, replacement in zip(dot_indices, combo):
            temp_list[index] = replacement
        possible_strings.append("".join(temp_list))

    return possible_strings

def get_window(i, j, matrix):
    content = ""
    for i1 in range(i, i+3):
        for j1 in range(j, j+3):
            content += matrix[i1][j1]
    return content

def get_sliding_windows_of_3x3(matrix):
    list_of_contents = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i+2 < len(matrix) and j+2 < len(matrix[0]):
                list_of_contents.append(get_window(i, j, matrix))
    return list_of_contents



INPUT_FILE = "input.txt"
SAMPLE_INPUT = "sample_input.txt"

with open(INPUT_FILE) as f:
    m = [list(line.strip()) for line in f]
    part1 = check_row(m) + check_verticals(m) + check_diagonals(m)
    print(f"Part1: {part1}")

"""
M.S     M.M     S.M     S.S
.A.     .A.     .A.     .A.
M.S     S.S     S.M     M.M
"""
patterns = ["M.S.A.M.S", "M.M.A.S.S", "S.M.A.S.M", "S.S.A.M.M"]
possiblities = [p for pattern in patterns for p in generate_possibilities(pattern)]
b = get_sliding_windows_of_3x3(m)
part2 = [x for x in b if x in possiblities]
print(f"Part2: {len(part2)}")