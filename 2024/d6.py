import tqdm

from utils.utils import MatrixOperations

SAMPLE_INPUT = "sample_input.txt"
INPUT = "input.txt"

requirements = []
updates = []

with open(INPUT, "r") as f:
    m = [list(line.strip()) for line in f]
    m_ops = MatrixOperations(matrix=m)

init_pos = m_ops.find_index("^")
visited_steps = []
init_dir = "up"
total_steps = 0
path = set()
way = []


def get_next_item(curr_pos, curr_dir, given_matrix):
    x = curr_pos[0]
    y = curr_pos[1]
    x_ = -1
    y_ = -1
    next_dirs = {
        "up": "right",
        "right": "down",
        "down": "left",
        "left": "up"
    }
    if curr_dir == "up":
        x_ = x - 1
        y_ = y
    elif curr_dir == "down":
        x_ = x + 1
        y_ = y
    elif curr_dir == "left":
        x_ = x
        y_ = y - 1
    elif curr_dir == "right":
        x_ = x
        y_ = y + 1
    if terminal_condition([x_, y_], given_matrix):
        return [x_, y_], curr_dir
    elif given_matrix[x_][y_] == "#":
        return [x, y], next_dirs[curr_dir]
    return [x_, y_], curr_dir

def terminal_condition(curr_pos, given_matrix):
    x = curr_pos[0]
    y = curr_pos[1]
    return x < 0 or x >= len(given_matrix) or y < 0 or y >= len(given_matrix[0])

def traverse(start_pos, start_dir, given_matrix):
    curr_pos = start_pos
    curr_dir = start_dir
    while not terminal_condition(curr_pos, given_matrix):
        path.add(tuple(curr_pos))
        way.append(tuple(list(curr_pos)+[curr_dir]))
        curr_pos, curr_dir = get_next_item(curr_pos, curr_dir, given_matrix)


traverse(init_pos, init_dir, m_ops.matrix)
print(f"Part1: {len(path)}")

# Part 2
def loop_exists(start_pos, start_dir, given_matrix):
    curr_pos = start_pos
    curr_dir = start_dir
    while_count = 0
    visited_steps = []
    while not terminal_condition(curr_pos, given_matrix):
        while_count += 1
        if while_count > len(given_matrix[0]) * len(given_matrix):
            return True
        curr_pos, curr_dir = get_next_item(curr_pos, curr_dir, given_matrix)
        if curr_pos+[curr_dir] in visited_steps:
            return True
        visited_steps.append(curr_pos+[curr_dir])
    return False

def get_candidates(list_of_point_and_dir, given_matrix):
    candidates = set()
    for x, y in list(set([z[:2] for z in list_of_point_and_dir])):
        possible_candidates = [[x-1, y], [x+1, y], [x, y-1], [x, y+1], [x, y]]
        for z in [a for a in possible_candidates if not terminal_condition(a, given_matrix) and given_matrix[x][y] != "#" and a != init_pos]:
            candidates.add(tuple(z))
    return candidates


import concurrent.futures

loopitems = set()

import concurrent.futures, time

loopitems = set()

def process_candidate(candidate):
    i, j = candidate
    new_copy = m_ops.deep_copy_matrix()
    new_copy[i][j] = "#"
    if loop_exists(init_pos, init_dir, new_copy):
        return (i, j)
    return None

start_time = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(process_candidate, candidate) for candidate in get_candidates(way, m_ops.matrix)]
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        if result:
            loopitems.add(result)

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(f"Part2: {len(loopitems)}")