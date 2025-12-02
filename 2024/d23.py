from utils.utils import Graph

g = Graph()
with open("input.txt") as f:
    for line in f:
        data = line.strip()
        t1, t2 = data.split("-")
        g.add_edge(t1, t2)

connected_3 = g.connected_nodes()
x = [x for x, y, z in connected_3 if x.startswith("t") or y.startswith("t") or z.startswith("t")]
print(len(x))

longest_clique = max(g.find_cliques(), key=len)
print(",".join(sorted(longest_clique)))