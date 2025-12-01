from typing import List, Tuple


FILE_NAME = 'input.txt'
INIT_STATE = 50
DIAL_SIZE = 100


def left_turn(state: int, clicks: int) -> Tuple[int, int]:
    raw_turn = state - clicks
    start_at_zero_offset = 1 if state == 0 else 0
    zero_passes = (-1 * raw_turn + DIAL_SIZE) // DIAL_SIZE
    return zero_passes - start_at_zero_offset, raw_turn % DIAL_SIZE


def right_turn(state: int, clicks: int) -> Tuple[int, int]:
    raw_turn = state + clicks
    zero_passes = raw_turn // DIAL_SIZE
    return zero_passes, raw_turn % DIAL_SIZE


def parse() -> List[Tuple[str, int]]:
    """
    Parse the input file into a list of tuples (op, clicks)
    where op is either L or R, and clicks is the integer number of clicks to turn
    """
    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()

    return [
        (line[0], int(line[1:])) for line in lines
    ]


def count_zeros_silver() -> int:
    state = INIT_STATE
    turns = parse()

    num_zeros = 0
    for op, clicks in turns:
        if op == 'L':
            _, state = left_turn(state, clicks)
        else:
            _, state = right_turn(state, clicks)

        if state == 0:
            num_zeros += 1

    return num_zeros


def count_zeros_gold() -> int:
    state = INIT_STATE
    turns = parse()

    num_zeros = 0
    for op, clicks in turns:
        if op == 'L':
            passes, state = left_turn(state, clicks)
        else:
            passes, state = right_turn(state, clicks)

        num_zeros += passes

    return num_zeros


if __name__ == "__main__":
    silver = count_zeros_silver()
    print(f"Silver: {silver}")
    gold = count_zeros_gold()
    print(f"Gold: {gold}")