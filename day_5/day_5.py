FILE_NAME = "input.txt"

def parse():
    with open(FILE_NAME) as f:
        fresh_ranges = []

        line = f.readline()
        while line.strip() != "":
            start, end = line.strip().split("-")
            fresh_ranges.append(
                (int(start), int(end))
            )
            line = f.readline()

        ingredient_ids = []
        line = f.readline()
        while line:
            ingredient_ids.append(int(line.strip()))
            line = f.readline()

        return fresh_ranges, ingredient_ids


def count_fresh_ingredients():
    fresh_ranges, ingredient_ids = parse()

    fresh_count = 0
    for ingredient_id in ingredient_ids:
        for start, end in fresh_ranges:
            if start <= ingredient_id <= end:
                fresh_count += 1
                break

    return fresh_count


def overlap(start_a, end_a, start_b, end_b):
    return not(end_a < start_b or end_b < start_a)


def count_fresh_inventory():
    fresh_ranges, _ = parse()

    range_list = []
    while len(fresh_ranges) > 0:
        start_a, end_a = fresh_ranges.pop()
        found_overlap = False
        for start_b, end_b in range_list:
            if overlap(start_a, end_a, start_b, end_b):
                range_list.remove((start_b, end_b))
                fresh_ranges.append((min(start_a, start_b), max(end_a, end_b)))
                found_overlap = True
                break

        if not found_overlap:
            range_list.append((start_a, end_a))

    fresh_count = 0
    for start, end in range_list:
        fresh_count += end - start + 1

    return fresh_count


if __name__ == "__main__":
    silver = count_fresh_ingredients()
    print(f"Silver: {silver}")
    gold = count_fresh_inventory()
    print(f"Gold: {gold}")