from collections import defaultdict

FILE_NAME = "input.txt"


def parse():
    start = None
    with open(FILE_NAME) as f:
        lines = f.readlines()
        start = lines[0].index("S")
    return start, lines[1:]


def count_splits():
    start, split_map = parse()
    cols = {start: 1}
    num_splits = 0
    for line in split_map:
        new_cols = defaultdict(int)
        for beam, beam_count in cols.items():
            if line[beam]  == "^":
                new_cols[beam - 1] += beam_count
                new_cols[beam + 1] += beam_count
                num_splits += 1
            else:
                new_cols[beam] += beam_count
        cols = new_cols
    return num_splits, sum(cols.values())


if __name__ == "__main__":
    silver, gold = count_splits()
    print(f"Silver: {silver}")
    print(f"Gold: {gold}")