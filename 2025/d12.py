filename = "input.txt"

shapes = []
grids = {}
sizes = {}
with open(filename) as f:
    shape_reader = False
    curr_shape = []
    for line in f:
        if ":" in line and "x" not in line:
            shape_reader = True
            curr_shape = []
        elif line == "\n":
            shapes.append(curr_shape)
            shape_reader = False
            curr_shape = []
        elif ":" in line and "x" in line:
            grid_size_str, shapes_to_fit = line.strip().split(":")
            grid_name = tuple(map(int, grid_size_str.split("x")))
            if grid_name not in grids:
                grids[grid_name] = []
            grids[grid_name].append(list(map( int, shapes_to_fit.strip().split())))
        elif shape_reader:
            curr_shape.append([x for x in line.strip()])

count = [0]*len(shapes)
for i, s in enumerate(shapes):
    for line in s:
        count[i] += line.count("#")
        print(line, count)
    if i not in sizes:
        sizes[i] = 0
    sizes[i] = count[i]

fittable_regions = 0
skipped_regions = 0
for grid in grids:
    total_spaces = grid[0]*grid[1]
    for region in grids[grid]:
        occupied_spaces = 0
        for ix in range(len(region)):
            occupied_spaces += (region[ix] * sizes[ix])
        ratio = occupied_spaces/total_spaces
        print(f"{occupied_spaces}/{total_spaces}\t{ratio*100:.2f}")
        if occupied_spaces >= total_spaces:
            skipped_regions += 1
            continue
        else:
            fittable_regions += 1

print(fittable_regions, skipped_regions)