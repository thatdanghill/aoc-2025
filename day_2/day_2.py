FILE_NAME = "input.txt"


def parse():
    with open(FILE_NAME) as f:
        linestr = f.readline().strip()
    id_ranges = linestr.split(",")
    return [tuple(id_range.split("-")) for id_range in id_ranges]


def find_silver_repetitions(id_ranges):
    matches = []
    for low, high in id_ranges:
        if len(low) % 2 != 0:
            low = str(10 ** len(low))

        half_low = len(low) // 2
        cur_fh = low[0:half_low]
        cur_guess = int(cur_fh * 2)
        while cur_guess < int(low):
            cur_fh = str(int(cur_fh) + 1)
            cur_guess = int(cur_fh * 2)

        while cur_guess <= int(high):
            matches.append(cur_guess)
            cur_fh = str(int(cur_fh) + 1)
            cur_guess = int(cur_fh * 2)
    return matches


def find_reps_with_len(rep_len, num_reps, low, high):
    matches = []

    cur_rep = str(low)[:rep_len]
    cur_val = int(cur_rep * num_reps)
    while cur_val < low and len(str(cur_rep)) == rep_len:
        cur_rep = str(int(cur_rep) + 1)
        cur_val = int(cur_rep * num_reps)

    while cur_val <= high and len(str(cur_rep)) == rep_len:
        matches.append(cur_val)
        cur_rep = str(int(cur_rep) + 1)
        cur_val = int(cur_rep * num_reps)

    return matches


def find_const_len_repetitions(low, high):
    length = len(str(low))
    rep_len = 1
    matches = []
    while rep_len <= len(str(high)) // 2 + 1:
        if length % rep_len == 0:
            num_reps = length // rep_len
            if num_reps != 1:
                matches += find_reps_with_len(rep_len, num_reps, low, high)
        rep_len += 1
    return matches


def find_all_repetitions(id_ranges):
    matches = []
    for low, high in id_ranges:
        cur_len = len(low)
        cur_low = int(low)
        while cur_len <= len(high):
            matches += find_const_len_repetitions(
                cur_low, min(int(high), 10**cur_len - 1)
            )
            cur_low = 10**cur_len
            cur_len += 1
    return matches


def sum_invalids_silver():
    id_ranges = parse()
    reps = find_silver_repetitions(id_ranges)
    return sum(reps)


def sum_invalids_gold():
    id_ranges = parse()
    reps = find_all_repetitions(id_ranges)
    return sum(set(reps))


if __name__ == "__main__":
    silver = sum_invalids_silver()
    print(f"Silver: {silver}")
    gold = sum_invalids_gold()
    print(f"Gold: {gold}")
