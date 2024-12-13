from utils.utils import MatrixOperations

SAMPLE_INPUT = "sample_input.txt"
INPUT = "input.txt"

all_nodes = dict()

with open(SAMPLE_INPUT, "r") as f:
    m = [list(line.strip()) for line in f]
    m_ops = MatrixOperations(matrix=m)

def flood_fill(matrix, start_i, start_j):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    start_val = matrix[start_i][start_j]
    visited = set()
    stack = [(start_i, start_j)]
    region = []
    perimeter = 0
    edges = set()
    points_in_region = set()

    while stack:
        i, j = stack.pop()
        if (i, j) not in visited:
            visited.add((i, j))
            region.append((i, j))
            points_in_region.add((i, j))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    if matrix[ni][nj] == start_val and (ni, nj) not in visited:
                        stack.append((ni, nj))
                    elif matrix[ni][nj] != start_val:
                        perimeter += 1
                        edges.add(frozenset({(i, j), (ni, nj)}))
                else:
                    perimeter += 1
                    edges.add(frozenset({(i, j), (ni, nj)}))

    return len(region), perimeter, edges, visited, points_in_region

def calculate_areas_and_perimeters(matrix):
    unique_values = set(val for row in matrix for val in row)
    results = {}

    for val in unique_values:
        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == val and (i, j) not in visited:
                    area, perimeter, edges, region, _ = flood_fill(matrix, i, j)
                    sides = edges
                    results[val] = results.get(val, []) + [(area, perimeter, sides, _)]
                    visited.update(region)
    return results

def calculate_total_sides(edges):
    # Convert frozensets to sorted tuples for easier processing
    sorted_edges = [tuple(sorted(edge)) for edge in edges]

    # Function to determine the direction between two points
    def direction(p1, p2):
        if p1[0] == p2[0]:
            return 'vertical'
        elif p1[1] == p2[1]:
            return 'horizontal'
        else:
            return 'diagonal'

    # Sort edges to process them in order
    sorted_edges.sort()

    # Initialize the previous direction
    prev_direction = None
    total_sides = 0

    for edge in sorted_edges:
        p1, p2 = edge
        current_direction = direction(p1, p2)

        # If the direction changes, increment the side count
        if current_direction != prev_direction:
            total_sides += 1

        # Update the previous direction
        prev_direction = current_direction

    return total_sides

def calculate_enclosed_edges(points):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    edges = set()

    for point in points:
        for di, dj in directions:
            neighbor = (point[0] + di, point[1] + dj)
            if neighbor in points:
                edge = frozenset({point, neighbor})
                edges.add(edge)

    return len(edges)

# Example usage
cost1 = 0
cost2 = 0
results = calculate_areas_and_perimeters(m_ops.matrix)
for k, v in results.items():
    print(k)
    for x in v:
        sides = calculate_total_sides(x[2]) - 1
        cost2 += (calculate_enclosed_edges(x[3])*x[0])
        print(sides, v)
    cost1 += sum([x[0]*x[1] for x in v])
print(cost1, cost2)