import heapq


def matrix_to_string(matrix):
    return ''.join(''.join(row) for row in matrix)


class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix

    def get_matrix_size(self):
        return len(self.matrix), len(self.matrix[0])

    def transpose_matrix(self):
        return [list(row) for row in zip(*self.matrix)]

    def flip_horizontally(self):
        return [row[::-1] for row in self.matrix]

    def flip_vertically(self):
        return self.matrix[::-1]

    def coordinates_after_horizontal_flip(self, x, y):
        return x, len(self.matrix[0]) - 1 - y

    def coordinates_after_vertical_flip(self, x, y):
        return len(self.matrix) - 1 - x, y

    def coordinates_after_transpose(self, x, y):
        return y, x

    def get_sliding_windows_m_by_n(self, m, n):
        windows = []
        rows, cols = len(self.matrix), len(self.matrix[0])
        for i in range(rows - m + 1):
            for j in range(cols - n + 1):
                window = [row[j:j + n] for row in self.matrix[i:i + m]]
                windows.append(window)
        return windows

    def pretty_print(self):
        for row in self.matrix:
            print('\t'.join(row))

    def find_index(self, item):
        for i, row in enumerate(self.matrix):
            if item in row:
                return tuple([i, row.index(item)])

    def find_all_indices(self, item):
        indices = []
        for i, row in enumerate(self.matrix):
            for j, col in enumerate(row):
                if col == item:
                    indices.append((i, j))
        return indices

    def find_total_occurrences(self, item):
        return sum([row.count(item) for row in self.matrix])

    def deep_copy_matrix(self):
        return [row[:] for row in self.matrix]

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = set()
        if node2 not in self.graph:
            self.graph[node2] = set()
        self.graph[node1].add(node2)
        self.graph[node2].add(node1)

    def display_graph(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {', '.join(map(str, neighbors))}")

    def connected_nodes(self):
        final_res = set()
        for node, items in self.graph.items():
            if len(items) < 2:
                continue
            items = list(items)
            for i , n1 in enumerate(items):
                for j, n2 in enumerate(items[i+1:]):
                    if self.is_connected(n1, [n2]) and self.is_connected(node, [n1]) and self.is_connected(node, [n2]):
                        final_res.add(tuple(sorted([node, n1, n2])))
        return final_res

    def is_connected(self, n1, list_of_nodes):
        if n1 in self.graph and all([n in self.graph for n in list_of_nodes]):
            return all([n1 in self.graph[n2] for n2 in list_of_nodes] + [n2 in self.graph[n1] for n2 in list_of_nodes])
        return False

    def bron_kerbosch(self, r, p, x, cliques):
        if not p and not x:
            cliques.append(r)
            return
        for node in list(p):
            new_r = r.union([node])
            new_p = p.intersection(self.graph[node])
            new_x = x.intersection(self.graph[node])
            self.bron_kerbosch(new_r, new_p, new_x, cliques)
            p.remove(node)
            x.add(node)

    def find_cliques(self):
        cliques = []
        self.bron_kerbosch(set(), set(self.graph.keys()), set(), cliques)
        return cliques

class Dijkstra:
    def __init__(self, matrix, start, end):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.start = start
        self.goal = end
        self.dist = {self.start: 0}
        self.prev = {}
        self.queue = [(0, self.start)]
        self.visited = set()

    def get_neighbors(self, node):
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = node[0] + dx, node[1] + dy
            if 0 <= x < self.rows and 0 <= y < self.cols and self.matrix[x][y] != "#":
                neighbors.append((x, y))
        return neighbors

    def reconstruct_path(self, current):
        path = [current]
        while current in self.prev:
            current = self.prev[current]
            path.append(current)
        path.reverse()
        return path

    def search(self):
        while self.queue:
            current_dist, current = heapq.heappop(self.queue)
            if current in self.visited:
                continue
            self.visited.add(current)
            if current == self.goal:
                return self.reconstruct_path(current)
            for neighbor in self.get_neighbors(current):
                distance = current_dist + 1
                if distance < self.dist.get(neighbor, float('inf')):
                    self.dist[neighbor] = distance
                    self.prev[neighbor] = current
                    heapq.heappush(self.queue, (distance, neighbor))
        return None