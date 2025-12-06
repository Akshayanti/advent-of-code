from utils.utils import MatrixOperations

filename = 'input.txt'

data = []
p2 = []
with open(filename, 'r') as f:
    for line in f:
        line = line.strip("\n")
        p2.append(line)
        line = line.strip().split()
        if line[0] not in ["*", "+"]:
            data.append([int(x) for x in line])
        else:
            data.append(line)

p1_total = 0

def do_the_math(matrix):
    total = 0
    for col in range(len(matrix[0])):
        mul_total=1
        add_total=0
        for row in range(len(matrix)):
            if type(matrix[row][col]) == int:
                add_total += matrix[row][col]
                mul_total *= matrix[row][col]
            elif type(matrix[row][col]) == str:
                if matrix[row][col] == "*":
                    total += mul_total
                else:
                    total += add_total
    return total

print(f"p1: {do_the_math(data)}")

# Begin p2
data = []
item_len = max([len(x) for x in p2])
for col in range(item_len):
    z = []
    for x in p2:
        z.append(x[col] if col < len(x) else " ")
    if not all([x == " " for x in z]):
        z = [x if x != ' ' else '0' for x in z]
    data.append(z)

d = MatrixOperations(data)
p2 = []
for x in d.transpose_matrix():
    p2.append(x)

for x in range(len(p2)):
    if p2[x][0] in ["*", "+"]:
        p2[x] = [f for f in "".join(p2[x]).replace("0", " ")]
    else:
        p2[x] =[f for f in "".join(p2[x])]

d = MatrixOperations(p2)
data = []
for x in d.transpose_matrix():
    data.append(x)

p2_total = 0
add_total = 0
mul_total = 1
symbol = "-"
for i in range(len(data)):
    if all([x == " " for x in data[i]]):
        if symbol == "*":
            p2_total += mul_total
        elif symbol == "+":
            p2_total += add_total
        symbol = "-"
        mul_total = 1
        add_total = 0
    else:
        num = int("".join(data[i][:-1]))
        for j in range(len(data[0])-2, 0, -1):
            if num % pow(10, j) == 0:
                num = num // pow(10, j)
        add_total += num
        mul_total *= num
        symbol = data[i][-1] if symbol == "-" else symbol
if symbol == "+":
    p2_total += add_total
elif symbol == "*":
    p2_total += mul_total

print(f"p2: {p2_total}")

