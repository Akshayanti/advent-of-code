from collections import deque

try:
    import tqdm
except ImportError:
    tqdm = None

# filename = "sample.txt"
filename = "input.txt"

end_states = []
joltages = []
all_switches = []

def get_data(file_to_open):
    with open(file_to_open) as f:
        for line in f:
            line_split = line.strip().split()
            end_state = ([x == "#" for x in line_split[0].strip("[").strip("]")])
            joltages = [int(a) for a in line_split[-1].strip("{").strip("}").split(",")]
            all_switches = []
            for x in line_split[1:len(line_split)-1]:
                all_switches.append([int(z) for z in x.strip("(").strip(")").split(",")])
            yield end_state, joltages, all_switches


def on_or_off(state, indices_to_flip):
    state_list = list(state)
    for idx in indices_to_flip:
        state_list[idx] = not state_list[idx]
    return tuple(state_list)

def get_min_switches_with_bfs(start_state, goal_state, switches, func):
    if start_state == goal_state:
        return 0

    queue = deque([(start_state, 0)])
    visited = {start_state}
    while queue:
        current_state, presses = queue.popleft()

        for switch in switches:
            next_state = func(current_state, switch)

            if next_state == goal_state:
                return presses + 1

            if any([current_state[x] > goal_state[x] for x in range(len(current_state)) if type(current_state[x]) == int]):
                continue

            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, presses + 1))

    return None


p1 = 0
p2 = 0

data_iter = get_data(filename)
if tqdm:
    data_iter = tqdm.tqdm(data_iter)

for on_status_final, joltage_final, switches in data_iter:
    on_status_init = tuple([False] * len(on_status_final))
    joltages_init = tuple([0] * len(joltage_final))

    # Part 1
    p1_min_presses = get_min_switches_with_bfs(on_status_init, tuple(on_status_final), switches, on_or_off)

    if p1_min_presses is not None:
        p1 += p1_min_presses

print(p1, p2)