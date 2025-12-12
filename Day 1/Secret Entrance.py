def file_to_list(filename = "input.txt"):
    with open(filename, "r") as file:
        # .strip() removes whitespace characters from both ends of the string
        content = [line.strip() for line in file.readlines() if line.strip()]
    return content


if __name__ == '__main__':
    moves_list = file_to_list()
    zero_counter = 0
    index = 50
    for move in moves_list:
        direction = move[0]
        distance = int(move[1:])

        if direction == "R":
            index = (index + distance) % 100
        elif direction == "L":
            index = (index - distance) % 100

        # print(index, direction, distance)

        if index == 0:
            zero_counter += 1

    print(zero_counter)