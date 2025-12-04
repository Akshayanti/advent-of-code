from utils.utils import MatrixOperations

filename = "input.txt"

matrix = []
with open(filename) as f:
    for line in f:
        matrix.append([x for x in line.strip()])

def count_rolls_in_neighbors(list_of_neighbors, symbol):
    n_vals = []
    for nx, ny in list_of_neighbors:
        n_vals.append(matrix[nx][ny])
    return n_vals.count(symbol)

p1_count = 0
symbol = "@"

mx = MatrixOperations(matrix)
print(mx.find_total_occurrences(symbol))
for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        if matrix[x][y] == symbol:
            n = mx.get_neighbor_cells(x, y, True)
            n_count = count_rolls_in_neighbors(n, symbol)
            if n_count < 4:
                p1_count += 1
print(p1_count)


p2_count = 0
while True:
    turn_count = 0
    mx = MatrixOperations(matrix)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == symbol:
                n = mx.get_neighbor_cells(x, y, True)
                n_count = count_rolls_in_neighbors(n, symbol)
                if n_count < 4:
                    p2_count += 1
                    turn_count += 1
                    matrix[x][y] = "."
    if turn_count == 0:
        break
print(p2_count)
