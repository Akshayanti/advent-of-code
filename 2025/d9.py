import tqdm
from shapely.geometry.polygon import Polygon

# filename = "sample.txt"

filename = "input.txt"

coords = []

with open(filename) as f:
    for line in f:
        y, x = map(int, line.strip().split(","))
        coords.append((x, y))

p1 = -1
for i, a in enumerate(coords):
    for b in coords[i:]:
        if a == b:
            continue
        x1, y1 = a
        x2, y2 = b
        # Correct area calculation: include both endpoints
        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        area = width * height
        p1 = max(area, p1)
print(f"P1: {p1}")

p2 = -1
done = []
for i, a in tqdm.tqdm(enumerate(coords)):
    for b in coords[i:]:
        if a == b:
            continue
        x1, y1 = a
        x2, y2 = b
        if (x1, y1, x2, y2) in done or (x2, y2, x1, y1) in done:
            continue
        polygon = Polygon([x for x in coords])
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)
        done.append((x1, y1, x2, y2))
        if polygon.contains(
                Polygon([(x_min, y_min), (x_max, y_min), (x_max, y_max), (x_min, y_max)])
        ):
            leng = abs(x1 - x2)+1
            bread = abs(y1 - y2)+1
            p2 = max(leng * bread, p2)
print(f"P2: {p2}")

