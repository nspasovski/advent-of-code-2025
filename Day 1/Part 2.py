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
        steps_to_hit = 0

        if direction == "R":
            steps_to_hit = 100 - index
            index = (index + distance) % 100

        elif direction == "L":
            steps_to_hit = index if index != 0 else 100 # if index is at 0, then it needs 100 moves to reach 0
            index = (index - distance) % 100


        if distance >= steps_to_hit:
            zero_counter += 1 + (distance - steps_to_hit) // 100

        # print(f'{move},ix= {index}, z= {zero_counter}')

    print(zero_counter)


