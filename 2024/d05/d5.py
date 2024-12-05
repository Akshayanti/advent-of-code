SAMPLE_INPUT = "sample_input.txt"
INPUT = "input.txt"

requirements = []
updates = []

with open(INPUT, "r") as f:
    for x in f.readlines():
        if "|" in x:
            requirements.append(x.strip().split("|"))
        if x == "\n":
            continue
        if "," in x:
            updates.append(x.strip().split(","))


def check_condition(list_to_check, pair):
    x, y = pair
    if x in list_to_check and y in list_to_check:
        return list_to_check.index(x) < list_to_check.index(y)
    return True


def reorder_list(list_to_reorder, pair):
    x, y = pair
    if x in list_to_reorder and y in list_to_reorder:
        x_index = list_to_reorder.index(x)
        y_index = list_to_reorder.index(y)
        if x_index < y_index:
            return list_to_reorder
        else:
            list_to_reorder[x_index], list_to_reorder[y_index] = list_to_reorder[y_index], list_to_reorder[x_index]
            return list_to_reorder
    return list_to_reorder


mids_proper = []
mids_improper = []
proper_updates = []
improper_updates = []
for update in updates:
    valid_reqs = [req for req in requirements for x in update if x == req[1]]
    all_checked_conditions = [check_condition(update, req) for req in valid_reqs]
    if all(all_checked_conditions):
        proper_updates.append(update)
        mids_proper.append(update[len(update) // 2])
    else:
        improper_updates.append(update)

for update in improper_updates:
    valid_reqs = [req for req in requirements for x in update if x == req[1]]
    orig_update = update[::-1]
    while orig_update != update:
        orig_update = update.copy()
        for req in valid_reqs:
            update = reorder_list(update, req)
    mids_improper.append(update[len(update) // 2])

print(f"Part1: {sum([int(x) for x in mids_proper])}")
print(f"Part2: {sum([int(x) for x in mids_improper])}")
