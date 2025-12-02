import math
import re

from utils.utils import MatrixOperations

SAMPLE_INPUT = "sample_input.txt"
INPUT = "input.txt"

all_nodes = dict()

with open(INPUT, "r") as f:
    m = [list(line.strip()) for line in f]
    m_ops = MatrixOperations(matrix=m)

for i, row in enumerate(m_ops.matrix):
    for j, col in enumerate(row):
        pattern = (r"\d|[A-Z]|[a-z]")
        if re.match(pattern, col):
            if col not in all_nodes:
                all_nodes[col] = []
            all_nodes[col].append((i, j))


def euclidean_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))


def find_antinodes(val1, val2, max_x, max_y):
    final_nodes = []
    x_diff = val2[0] - val1[0]
    y_diff = val2[1] - val1[1]
    added_nodes_X = [val1[0] - x_diff, val2[0] + x_diff, val1[0] + x_diff, val2[0] - x_diff]
    added_nodes_Y = [val1[1] - y_diff, val2[1] + y_diff, val1[1] + y_diff, val2[1] - y_diff]
    for point in zip(added_nodes_X, added_nodes_Y):
        if 0 <= point[0] < max_x and 0 <= point[1] < max_y:
            dist_from_p1 = euclidean_distance(val1, point)
            dist_from_p2 = euclidean_distance(val2, point)
            if dist_from_p1 == 2 * dist_from_p2 or dist_from_p2 == 2 * dist_from_p1:
                final_nodes.append(point)
        else:
            continue
    return final_nodes


def find_antinodes2(val1, val2, max_x, max_y):
    final_nodes = []
    x_diff = val2[0] - val1[0]
    y_diff = val2[1] - val1[1]
    added_nodes_X = []
    added_nodes_Y = []
    for i in range(int(max_x / abs(x_diff)) + 2):
        for j in range(int(max_y / abs(y_diff)) + 2):
            added_nodes_X.append(val1[0] + i * x_diff)
            added_nodes_Y.append(val1[1] + j * y_diff)

            added_nodes_X.append(val1[0] - i * x_diff)
            added_nodes_Y.append(val1[1] - j * y_diff)

            added_nodes_X.append(val2[0] + i * x_diff)
            added_nodes_Y.append(val2[1] + j * y_diff)

            added_nodes_X.append(val2[0] - i * x_diff)
            added_nodes_Y.append(val2[1] - j * y_diff)

    for point in zip(added_nodes_X, added_nodes_Y):
        if point in final_nodes:
            continue
        if 0 <= point[0] < max_x and 0 <= point[1] < max_y:
            dist_from_p1 = euclidean_distance(val1, point)
            dist_from_p2 = euclidean_distance(val2, point)
            dist_p1_p2 = euclidean_distance(val1, val2)
            if round(abs(dist_from_p1 - dist_from_p2), 8) == round(dist_p1_p2, 8):
                final_nodes.append(point)
        else:
            continue
    return final_nodes


total_count = 0
all_anti_nodes = []
all_anti_nodes2 = []
for key, list_of_nodes in all_nodes.items():
    for i, node in enumerate(list_of_nodes):
        for j in range(i + 1, len(list_of_nodes)):
            nodes = find_antinodes(node, list_of_nodes[j], len(m_ops.matrix), len(m_ops.matrix[0]))
            nodes2 = find_antinodes2(node, list_of_nodes[j], len(m_ops.matrix), len(m_ops.matrix[0]))
            all_anti_nodes.extend(nodes)
            all_anti_nodes2.extend(nodes2)

print(f"Part1: {len(set(all_anti_nodes))}")
print(f"Part2: {len(set(all_anti_nodes2))}")
