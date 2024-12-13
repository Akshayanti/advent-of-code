import re

"""
Recommended Read: 
https://www.reddit.com/r/adventofcode/comments/1hd7irq/2024_day_13_an_explanation_of_the_mathematics/
"""
def process_input(input_path):
    prizes_and_buttons = dict()
    with open(input_path, "r") as f:
        lines = f.readlines()

    pattern_button = r"Button [A-B]: X\+(\d+), Y\+(\d+)"
    pattern_prize = r"Prize: X=(\d+), Y=(\d+)"

    vuttons = {}
    for line in lines:
        if line.startswith("Button"):
            match = re.search(pattern_button, line)
            if match:
                button = line.split(":")[0].strip("")
                x, y = map(int, match.groups())
                vuttons["A" if "A" in button else "B"] = (x, y)
        elif line.startswith("Prize"):
            match = re.search(pattern_prize, line)
            if match:
                x, y = map(int, match.groups())
                current_prize = (x, y)
                if vuttons:
                    prizes_and_buttons[current_prize] = vuttons
                    vuttons = {}
    for prizes, buttons in prizes_and_buttons.items():
        yield prizes[0], prizes[1], buttons['A'][0], buttons['A'][1], buttons['B'][0], buttons['B'][1]

def get_p1_values(x, y, x1, y1, x2, y2):
    det = x1 * y2 - y1 * x2
    a = int((x * y2 - y * x2) / det)
    b = int((x1 * y - y1 * x) / det)
    if a*x1 + b*x2 == x and a*y1 + b*y2 == y:
        return (a, b)
    else:
        return (0, 0)


def get_p2_values(x, y, x1, y1, x2, y2):
    to_add = 10_000_000_000_000
    return get_p1_values(x + to_add, y + to_add, x1, y1, x2, y2)

INPUT = "input.txt"
SAMPLE = "sample_input.txt"

cost_p1 = 0
cost_p2 = 0
for x, y, x1, y1, x2, y2 in process_input(INPUT):
    a, b = get_p1_values(x, y, x1, y1, x2, y2)
    cost_p1 += 3*a + b
    a, b  = get_p2_values(x, y, x1, y1, x2, y2)
    cost_p2 += 3*a + b
print(cost_p1, cost_p2)
