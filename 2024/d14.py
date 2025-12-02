import math


def predict_pos(pos_x, pos_y, vel_x, vel_y, time=100):
    new_pos_x = (pos_x + vel_x * time) % 101
    new_pos_y = (pos_y + vel_y * time) % 103
    return new_pos_x, new_pos_y

def process_file(input_file):
    with open(input_file, "r") as f:
        for line in f:
            p, v = line.strip().split(" ")
            p = tuple(p[2:].split(","))
            v = tuple(v[2:].split(","))
            yield p, v


def get_quads(bots, x_max, y_max):
    quads = [0,0,0,0]
    for pos_x, pos_y, _, _ in bots:
        if pos_x < x_max//2 and pos_y < y_max//2:
            quads[0]  += 1
        if pos_x > x_max//2 and pos_y < y_max//2:
            quads[1]  += 1
        if pos_x < x_max//2 and pos_y > y_max//2:
            quads[2]  += 1
        if pos_x > x_max//2 and pos_y > y_max//2:
            quads[3]  += 1
    return quads


INPUT_FILE = "input.txt"
SAMPLE_FILE = "sample_input.txt"

robots = []

for x, y in process_file(INPUT_FILE):
    robots.append([int(x[0]), int(x[1]), int(y[0]), int(y[1])])

init = robots.copy()
t = 0

# PART 1
i = 0
for px, py, vx, vy in robots:
    px, py  = predict_pos(px, py, vx, vy, 100)
    robots[i] = [px, py, vx, vy]
    i += 1
qs = get_quads(robots, 101, 103)
print(f"Part1: {math.prod(qs)}")


# PART 2
robots =  init.copy()
condition = False
while not condition:
    grid = [['-']*101 for _ in range(103)]
    i = 0
    t += 1
    for px, py, vx, vy in robots:
        px, py = predict_pos(px, py, vx, vy, 1)
        robots[i] = [px, py, vx, vy]
        grid[py][px] = '#'
        i += 1

    if any(['###########' in "".join(row) for row in grid]):
        print(f"Part2: {t}")
        for row in grid:
            print("".join(row))
        print()
    condition =  robots == init
