from collections import Counter

all_states = [50]
curr_state = 50
part2 = 0
with open('input.txt', 'r') as infile:
    for line in infile:
        if 'L' in line:
            val = int(line[line.index('L')+1:])
            part2 += val // 100
            val = val % 100
            new_dest = (curr_state - val)
            if new_dest <= 0 < curr_state:
                part2 += 1
            curr_state = new_dest
        elif 'R' in line:
            val = int(line[line.index('R')+1:])
            part2 += val // 100
            val = val % 100
            new_dest = (curr_state + val)
            if curr_state < 100 <= new_dest:
                part2 += 1
            curr_state = new_dest
        all_states.append(curr_state%100)
        curr_state = all_states[-1]

l_to_d = Counter()
l_to_d.update(all_states)
print(l_to_d)
print(part2)
