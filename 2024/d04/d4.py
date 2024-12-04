import re

from utils.utils import MatrixOperations, matrix_to_string


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

m_ops = MatrixOperations(matrix=m)
b = [matrix_to_string(window) for window in m_ops.get_sliding_windows_m_by_n(m=3, n=3)]
part2 = [x for x in b if bool(re.fullmatch(r"|".join(patterns), x))]
print(f"Part2: {len(part2)}")