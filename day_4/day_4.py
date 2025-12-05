FILE_NAME = "input.txt"


def parse():
    with open(FILE_NAME) as file:
        return [
            list(line.strip())
            for line in file
        ]


def forklift_accessible(i, j, room, height, width):
    count_spots = 0
    # Upper left
    count_spots += (i > 0 and j > 0 and room[i - 1][j - 1] == "@")
    # Upper middle
    count_spots += (i > 0 and room[i - 1][j] == "@")
    # Upper right
    count_spots += (i > 0 and j < width - 1 and room[i - 1][j + 1] == "@")
    # Left
    count_spots += (j > 0 and room[i][j - 1] == "@")
    # Right
    count_spots += (j < width - 1 and room[i][j + 1] == "@")
    # Lower left
    count_spots += (i < height - 1 and j > 0 and room[i + 1][j - 1] == "@")
    # Lower middle
    count_spots += (i < height - 1 and room[i + 1][j] == "@")
    # Lower right
    count_spots += (i < height - 1 and j < width - 1 and room[i + 1][j + 1] == "@")

    return count_spots < 4


def accessible_rolls(room):
    height = len(room)
    width = len(room[0])

    accessible = []
    for i, row in enumerate(room):
        for j, col in enumerate(row):
            if col == "@" and forklift_accessible(i, j, room, height, width):
                accessible.append((i, j))

    return accessible


def update_room(room, rolls_to_remove):
    for i, j in rolls_to_remove:
        room[i][j] = "."
    return room


def num_accessible_silver():
    room = parse()
    return len(accessible_rolls(room))


def num_acessible_gold():
    room = parse()

    accessible = 0
    while True:
        to_remove = accessible_rolls(room)
        room = update_room(room, to_remove)
        accessible += len(to_remove)
        if len(to_remove) == 0:
            break
    return accessible


if __name__ == '__main__':
    silver = num_accessible_silver()
    print(f"Silver: {silver}")
    gold = num_acessible_gold()
    print(f"Gold: {gold}")