import tqdm

from utils.utils import Graph

filename = "input.txt"
# filename = "sample.txt"


def find_all_paths(graph, start, end):
    paths = []
    if start == end:
        return paths
    paths.append(start)
    for node in graph.get_node_by_val(start):
        if node == end:
            return paths
        path = find_all_paths(graph, node, end)
        paths.extend(path)


G = Graph()
with open(filename) as f:
    for line in f:
        parent, children = line.split(": ")
        for x in children.strip().split():
            G.add_edge(parent, x, False)

# part 1
all_paths = [x for x in G.find_all_paths("you", "out")]
print("p1", len(all_paths))

# part 2
# might take upwards of 10 days, lmfao
count = 0
for x in tqdm.tqdm(G.find_all_paths("svr", "out")):
    z = set(x)
    if "dac" in z and "fft" in z:
        count += 1
print("p2", count)