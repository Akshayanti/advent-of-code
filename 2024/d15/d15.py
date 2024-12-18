import re

from utils.utils import MatrixOperations

directions = {
    '<': (0, -1),
    '>': (0, 1),
    'v': (1, 0),
    '^': (-1, 0)
}

def read_file(file):
    matrix = []
    steps = []
    with open(file, 'r') as f:
        lines = f.readlines()
        matrix_part = True
        for line in lines:
            line = line.strip()
            if line == '':
                matrix_part = False
                continue
            if matrix_part:
                matrix.append(list(line))
            else:
                steps += list(line)
    return MatrixOperations(matrix), steps

def get_score(matrix, search_item):
    score = 0
    for i, j in matrix.find_all_indices(search_item):
        score += 100*i + j
    return score

SAMPLE = "sample_input.txt"
INPUT = "input.txt"
matrix, steps = read_file(INPUT)

# Part 1
def easy_step(new_pos, given_matrix):
    x, y = new_pos
    if x < 0 or x >= len(given_matrix.matrix) or y < 0 or y >= len(given_matrix.matrix[0]):
        return False
    if given_matrix.matrix[x][y] == '#':
        return False
    if given_matrix.matrix[x][y] == '.':
        return True
    return None

def can_step_to(new_pos, given_direction, given_matrix):
    x, y = new_pos
    z = easy_step(new_pos, given_matrix)
    if z is not None:
        return z
    row_of_interest = []
    new_direction = ''
    if given_direction in ['<', '>']:
        row_of_interest = given_matrix.matrix[x]
        new_direction = given_direction
    elif given_direction in ['^', 'v']:
        x, y = y, x
        row_of_interest = given_matrix.transpose_matrix()[x]
        new_direction = '>' if given_direction == 'v' else '<'
    if new_direction == '<':
        row_of_interest = row_of_interest[:y][::-1]
    else:
        row_of_interest = row_of_interest[y + 1:]
    return "." in row_of_interest

def move_stone (given_direction, given_matrix):

    def process_l_to_r():
        for i, row in enumerate(given_matrix.matrix):
            if '@' not in row:
                continue
            text = "".join(row)
            if re.findall(r'@O+#', text):
                return given_matrix
            moved_text = re.sub(r'@O+.', lambda match: '.@' + 'O' * (len(match.group()) - 2), text)
            given_matrix.matrix[i] = list(moved_text)
        return given_matrix

    if given_direction == ">":
        return process_l_to_r()
        # return z[0], z[1]
    elif given_direction == "<":
        # flip horizontally
        given_matrix.matrix = given_matrix.flip_horizontally()
        # process normally
        given_matrix = process_l_to_r()
        # flip back
        given_matrix.matrix = given_matrix.flip_horizontally()
        # get the new index after flip back
        return given_matrix
    elif given_direction == "v":
        # transpose
        given_matrix.matrix = given_matrix.transpose_matrix()
        # process normally
        given_matrix = process_l_to_r()
        # get the new index after transpose 3x
        given_matrix.matrix = given_matrix.transpose_matrix()
        given_matrix.matrix = given_matrix.transpose_matrix()
        given_matrix.matrix = given_matrix.transpose_matrix()
        return given_matrix
    elif given_direction == "^":
        # transpose
        given_matrix.matrix = given_matrix.transpose_matrix()
        # flip horizontally
        given_matrix.matrix = given_matrix.flip_horizontally()
        # process normally
        given_matrix = process_l_to_r()
        # flip back
        given_matrix.matrix = given_matrix.flip_horizontally()
        # transpose back 3x
        given_matrix.matrix = given_matrix.transpose_matrix()
        given_matrix.matrix = given_matrix.transpose_matrix()
        given_matrix.matrix = given_matrix.transpose_matrix()
        return given_matrix

def get_new_step(new_step, direction, matrix):
    x, y = new_step
    x0, y0 = matrix.find_index('@')
    if matrix.matrix[x][y] == '.':
        matrix.matrix[x0][y0], matrix.matrix[x][y] = matrix.matrix[x][y], matrix.matrix[x0][y0]
        return matrix
    else:
        return move_stone(direction, matrix)

def move_fish(given_direction, given_matrix):
    x, y = given_matrix.find_index('@')
    add_x, add_y = directions[given_direction]
    new_possible_step = (x + add_x, y + add_y)
    if can_step_to(new_possible_step, given_direction, given_matrix):
        return get_new_step(new_possible_step, given_direction, given_matrix)
    else:
        return given_matrix

for i, step in enumerate(steps):
    matrix = move_fish(step, matrix)
print(f"Part 1: {get_score(matrix, 'O')}")

# End part 1

# Part 2
def create_input(given_matrix):
    for i, row in enumerate(given_matrix):
        given_matrix[i] = list("".join(row).replace("#", "##")\
            .replace("O", "[]")\
            .replace(".", "..")\
            .replace("@", "@."))
    return given_matrix

def get_blocking_boxes(matrix, x, y, given_direction, visited=None):
    if visited is None:
        visited = set()

    if (x, y) in visited:
        return visited

    visited.add((x, y))

    dx, dy = given_direction
    nx, ny = x + dx, y + dy
    if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] in ['[', ']']:
        if matrix[nx][ny] == "[":
            get_blocking_boxes(matrix, nx, ny, given_direction, visited)
            get_blocking_boxes(matrix, nx, ny+1, given_direction, visited)
        elif matrix[nx][ny] == "]":
            get_blocking_boxes(matrix, nx, ny, given_direction, visited)
            get_blocking_boxes(matrix, nx, ny-1, given_direction, visited)
    return visited

def bot_can_move(given_direction, given_matrix):
    source = given_matrix.find_index('@')
    dx, dy = directions[given_direction]
    dest = (source[0]+dx, source[1]+dy)
    z = easy_step(dest, given_matrix)
    if z is not None:
        return z
    set_of_boxes = get_blocking_boxes(given_matrix.matrix, source[0], source[1], directions[given_direction]) - {source}
    z = all([given_matrix.matrix[f0+dx][f1+dy] != "#" for f0, f1 in set_of_boxes])
    return z


def move_box(box_pos, given_direction, given_matrix):
    dx, dy = directions[given_direction]
    x, y = box_pos
    x_ = x + dx
    y_ = y + dy
    given_matrix.matrix[x][y], given_matrix.matrix[x_][y_] = given_matrix.matrix[x_][y_], given_matrix.matrix[x][y]
    return given_matrix


def move_bot(given_direction, given_matrix):
    x, y = given_matrix.find_index('@')
    dx, dy = directions[given_direction]
    x_ = x + dx
    y_ = y + dy
    dest = (x+dx, y+dy)

    if easy_step(dest, given_matrix):
        given_matrix.matrix[x_][y_] = "@"
        given_matrix.matrix[x][y] = "."
        return given_matrix
    else:
        set_of_boxes = get_blocking_boxes(given_matrix.matrix, x, y, directions[given_direction])
        for box in sorted(set_of_boxes, reverse=False if given_direction in ['<', '^'] else True):
            move_box(box, given_direction, given_matrix)
        return given_matrix

def take_step(given_direction, given_matrix):
    if bot_can_move(given_direction, given_matrix):
        return move_bot(given_direction, given_matrix)
    return given_matrix

matrix, steps = read_file(INPUT)
matrix = MatrixOperations(create_input(matrix.matrix))
for i, step in enumerate(steps):
    matrix = take_step(step, matrix)
print(f"Part 2: {get_score(matrix, '[')}")