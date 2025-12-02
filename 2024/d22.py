from functools import lru_cache

import tqdm

@lru_cache(maxsize=None)
def calc_iter(x, counts = 2_000):
    for i in range(counts):
        x = (x*65) % 16777216
        b = x//32
        x = (x ^ b) % 16777216
        x = (x *2049) % 16777216
    return x

def get_seq(collection_of_inputs):
    x1 = None
    x2 = None
    x3 = None
    x4 = None
    sed_dict = {}
    for x in tqdm.tqdm(collection_of_inputs):
        num_dict = dict()
        prev_iter = calc_iter(x, 0)%10
        for i in range(1, 2_001):
            this_iter = calc_iter(x, i)%10
            z = this_iter - prev_iter
            x1, x2, x3, x4 = x2, x3, x4, z
            if x1 and x2 and x3 and x4:
                if (x1, x2, x3, x4) not in num_dict:
                    num_dict[(x1, x2, x3, x4)] = this_iter
            prev_iter = this_iter
        for z in num_dict:
            if z not in sed_dict:
                sed_dict[z] = num_dict[z]
            else:
                sed_dict[z] += num_dict[z]
    max_key = max(sed_dict, key=sed_dict.get)
    print(max_key, sed_dict[max_key])

inpuits = []
with open("input.txt") as f:
    for line in f:
        x = int(line.strip())
        inpuits.append(x)
print(sum([calc_iter(x, 2000) for x in inpuits]))
get_seq(inpuits)