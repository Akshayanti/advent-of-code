def matrix_to_string(matrix):
    return ''.join(''.join(row) for row in matrix)


class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix

    def transpose_matrix(self):
        return [list(row) for row in zip(*self.matrix)]

    def flip_horizontally(self):
        return [row[::-1] for row in self.matrix]

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
            print(' '.join(row))

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