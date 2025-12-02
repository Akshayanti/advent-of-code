from utils.utils import MatrixOperations
from utils.utils import Dijkstra

def read_input(filename):
    m = [[0 for _ in range(71)] for _ in range(71)]
    matrix = MatrixOperations(m)
    with open("input.txt") as f:
        for i, line in enumerate(f):
            cont = line.strip().split(",")
            x, y = int(cont[0]), int(cont[1])
            if i >= 1024:
                break
            matrix.matrix[x][y] = "#"
    return matrix

def get_all_possible_matrices(filename):
    m = [[0 for _ in range(71)] for _ in range(71)]
    with open(filename) as f:
        for i, line in enumerate(f):
            cont = line.strip().split(",")
            x, y = int(cont[0]), int(cont[1])
            m[x][y] = "#"
            yield MatrixOperations(m), x, y

# part 1
matrix = read_input("input.txt")
dk = Dijkstra(matrix.matrix, (0,0), (70,70))
path = dk.search()
if path:
    print("Part 1:", len(path) - 1)


# part 2
for matrix, x, y in get_all_possible_matrices("input.txt"):
    dk = Dijkstra(matrix.matrix, (0,0), (70,70))
    path = dk.search()
    if not path:
        print("Part 2:", ",".join([str(x), str(y)]))
        break
