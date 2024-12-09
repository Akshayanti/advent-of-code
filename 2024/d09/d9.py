import re

import tqdm

SAMPLE_INPUT = "sample_input.txt"
INPUT = "input.txt"

with open(INPUT, "r") as f:
    for line in f:
        val = line.strip()


def generate_string(given_input):
    out_String = ""
    for i, x in enumerate(given_input):
        file_id = int((i-1)/2 if i % 2 != 0 else i/2)
        out_String += f"{file_id}_"*int(x) if i % 2 == 0 else "."*int(x)
    return out_String

def find_last_index(given_string):
    matches = list(re.finditer(r"\d+_", given_string))
    return matches[-1].span() if matches else (-1, -1)

def move_frag(given_string):
    free_space = given_string.find(".")
    last_index_begin, last_index_end = find_last_index(given_string)
    if free_space >= last_index_begin:
        return given_string
    gs = list(given_string)
    gs[free_space] = "".join(given_string[last_index_begin:
                                  last_index_end-1]) + "_"
    gs[last_index_begin:last_index_end] = "."
    assert len("".join(gs)) == len(given_string)
    return "".join(gs)

def move_frags(given_string):
    while len(re.split(r'\.+', given_string)) > 2:
        given_string = move_frag(given_string)
    return given_string

def calc_checksum(given_string):
    check_sum = 0
    for i, x in enumerate(re.split(r'\_|\.', given_string)):
        if x == "":
            continue
        check_sum += int(x) * i
    return check_sum

def get_max_file_num(given_string):
    return max([int(x) for x in re.findall(r"\d+", given_string)])

def find_item_exactly_n_times(str_to_find_in, itm_to_find, n):
    pattern = re.compile(re.escape(itm_to_find * n))
    return sorted(list(pattern.finditer(str_to_find_in)), key=lambda x: x.start())

skip_counter = 0
def move_files(given_string):
    global skip_counter
    for i in tqdm.tqdm(range(get_max_file_num(given_string), -1, -1)):
        num_frags = given_string.count(f"{i}_")
        if num_frags == 0:
            skip_counter += 1
            continue
        file_index = given_string.find(f"{i}_")
        free_index = given_string.find("."*num_frags)
        if free_index >= file_index or free_index == -1 or file_index == -1:
            skip_counter += 1
            continue
        available_free_spaces = find_item_exactly_n_times(str_to_find_in=given_string,
                                                          itm_to_find=".",
                                                          n=num_frags)
        free_space_start, free_space_end = available_free_spaces[0].span()
        replacement_cand = f"{i}_"*num_frags
        new_copy = list(given_string)
        new_copy[file_index:file_index+len(replacement_cand)] = "."*num_frags
        new_copy[free_space_start:free_space_end] = replacement_cand
        assert len(given_string) == len("".join(new_copy))
        given_string = "".join(new_copy)
    return given_string

repr_string = generate_string(val)
print("INFO: String generated of length ", len(repr_string))
p1_string = move_frags(repr_string)
print("INFO: Frags moved")
print(f"Part1: {calc_checksum(p1_string)}")
p2_String = move_files(repr_string)
print(f"INFO: Files moved, could not move {skip_counter} files")
print(f"Part2: {calc_checksum(p2_String)}")