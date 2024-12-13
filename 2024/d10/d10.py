from utils.utils import MatrixOperations

SAMPLE_INPUT = "sample_input.txt"
INPUT = "input.txt"

all_nodes = dict()

with open(INPUT, "r") as f:
    m = [list(line.strip()) for line in f]
    m_ops = MatrixOperations(matrix=m)

def find_next_step(i, j, current_val, matrix):
    return_list = []
    if current_val == 9:
        return []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and int(matrix[ni][nj]) == current_val + 1:
            return_list.append((ni, nj))
    return return_list

def get_starting_points(matrix):
    out_list = []
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if int(matrix[i][j]) == 0:
                out_list.append((i, j))
    print(len(out_list), matrix.count("0"))
    return out_list

def find_path(start_points, matrix):
    all_paths = []
    for i, j in start_points:
        items = [(i, j, [(i, j)])]
        current_val = 0
        while items:
            next_items = []
            for i, j, path in items:
                next_steps = find_next_step(i, j, current_val, matrix)
                for ni, nj in next_steps:
                    new_path = path + [(ni, nj)]
                    if current_val + 1 == 9:
                        all_paths.append(new_path)
                    else:
                        next_items.append((ni, nj, new_path))
            current_val += 1
            items = next_items
    z = []
    z =  [x for x in all_paths if x not in z]
    # for x in z:
    #     print(x)
    return z

def find_trailhead_val(all_paths):
    out_dict = dict()
    for path in all_paths:
        start = path[0]
        end =  path[-1]
        if start not in out_dict:
            out_dict[start] = set()
        out_dict[start].add(end)
    return out_dict

all_paths = find_path(m_ops.find_all_indices("0"), m_ops.matrix)
all_nodes = find_trailhead_val(all_paths)
print(f"Part1: {sum([len(y) for x, y in all_nodes.items()])}")
print(f"Part2: {len(all_paths)}")
