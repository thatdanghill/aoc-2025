import math

FILE_NAME = "input.txt"

def parse_silver():
    row_list = []
    with open(FILE_NAME) as f:
        for line in f:
            row_list.append(line.strip().split())
    return list(zip(*row_list))


def sum_equations_silver():
    equations = parse_silver()

    total_sum = 0
    for equation in equations:
        numbers = [int(x) for x in equation[:-1]]
        if equation[-1] == "*":
            evaluation = math.prod(numbers)
        else:
            evaluation = sum(numbers)
        total_sum += evaluation
    return total_sum


def parse_gold():
    row_list = []
    with open(FILE_NAME) as f:
        lines = f.readlines()
        for line in lines[:-1]:
            row_list.append(list(line))
        ops = lines[-1].split()

    col_list = zip(*row_list)
    groups = []
    i = 0
    group = (ops[i], [])
    for col in col_list:
        if "".join(col).strip() == "":
            groups.append(group)
            i += 1
            if i != len(ops):
                group = (ops[i], [])
        else:
            group[1].append(int("".join(col)))

    return groups

def sum_equations_gold():
    equations = parse_gold()
    total_sum = 0
    for op, numbers in equations:
        if op == "*":
            evaluation = math.prod(numbers)
        else:
            evaluation = sum(numbers)
        total_sum += evaluation
    return total_sum

if __name__ == "__main__":
    silver = sum_equations_silver()
    print(f"Silver: {silver}")
    gold = sum_equations_gold()
    print(f"Gold: {gold}")