fileame = 'input.txt'

grid = []
with open(fileame, 'r') as f:
    for line in f:
        grid.append([x for x in line.strip()])

print(grid)

start_idx = (0, grid[0].index('S'))
idxes = set([start_idx])

while idxes != set():
    i = 1
    while i < len(grid):
        _, j = idxes.pop()
        i = _ + 1
        if i >= len(grid):
            break
        if grid[i][j] == '.':
            grid[i][j] = '|'
            idxes.add((i, j))
        elif grid[i][j] == '^':
            neighbors = [(0, -1), (0, 1)]
            for dx, dy in neighbors:
                if 0 <= j + dy < len(grid[0]) and grid[i][j + dy] == '.':
                    grid[i][j + dy] = '|'
                    idxes.add((i, j + dy))
            break
p1 = 0
for i in range(1, len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '^':
            if grid[i-1][j] == '|':
                p1 += 1
print(f"p1: {p1}")

# Begin Part 2 - Count quantum timelines
def count_timelines(grid, start):
    """
    Count all possible timelines (paths) from start to exit.
    Rules:
    - Always move straight down
    - If next cell is '.': continue straight
    - If next cell is '^': split to left and right of splitter (same row as '^')
    - If exit bottom: one timeline complete
    """
    rows, cols = len(grid), len(grid[0])
    memo = {}

    def dfs(r, c):
        # Out of bounds horizontally - this path ends
        if c < 0 or c >= cols:
            return 0

        # Exited bottom - one timeline complete
        if r >= rows:
            return 1

        # Check memo
        if (r, c) in memo:
            return memo[(r, c)]

        # Check next position
        next_r = r + 1

        if next_r >= rows:
            # Next step exits the bottom
            result = 1
        elif grid[next_r][c] == '^':
            # Hit a splitter - split into two paths
            # One path goes to left of splitter, one to right
            result = dfs(next_r, c - 1) + dfs(next_r, c + 1)
        else:
            # Empty space (., |, or S) - continue straight down
            result = dfs(next_r, c)

        memo[(r, c)] = result
        return result

    return dfs(start[0], start[1])

# Calculate total timelines
p2 = count_timelines(grid, start_idx)
print(f"p2: {p2}")