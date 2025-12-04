FILE_NAME = "input.txt"

def parse():
    with open(FILE_NAME) as f:
        return [
            [int(battery) for battery in bank.strip()]
            for bank in f
        ]


def get_max_bank_joltage(bank, num_vals):
    cur_bank = bank[:-(num_vals - 1)]

    jolt_str = ""
    for i in range(num_vals):
        next_val = max(cur_bank)
        next_index = cur_bank.index(next_val)

        jolt_str += str(next_val)
        cur_bank = cur_bank[next_index + 1:]
        cur_bank.append(bank[-(num_vals - i - 1)])

    return int(jolt_str)


def joltage(num_bats):
    batteries = parse()
    joltages = [
        get_max_bank_joltage(bank, num_bats)
        for bank in batteries
    ]
    return sum(joltages)


if __name__ == "__main__":
    silver = joltage(2)
    print(f"Silver: {silver}")
    gold = joltage(12)
    print(f"Gold: {gold}")