import copy


def file_to_list(filename = "input.txt"):
    with open(filename, "r") as file:
        # .strip() removes whitespace characters from both ends of the string
        content = [line.strip() for line in file.readlines() if line.strip()]
    return content


def accessible_paper_rolls(grid):
    accessible_rolls = 0

    # coordinates of the neighbouring cells
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    grid_copy = copy.deepcopy(grid) # for testing purpose

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            neighbor_rolls = 0

            if grid[r][c] == '@':
                for dr, dc in directions:
                    next_r, next_c = r + dr, c + dc
                    if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]) and grid[next_r][next_c] == '@': # if valid coord and has roll '@'
                        neighbor_rolls += 1

                if neighbor_rolls < 4:
                    accessible_rolls += 1

                    grid_copy[r][c] = 'X' # replacing an accessible roll with an X - for example purpose

    #printing the result - testing the example
    # for row in grid_copy:
    #     print("".join(row))
    #
    # print()

    if accessible_rolls == 0: # break case for recursion
        return 0

    return accessible_rolls + accessible_paper_rolls(grid_copy)


if __name__ == '__main__':
    rolls_grid = file_to_list()
    rolls_grid = [list(row) for row in rolls_grid]

    num_of_rolls = accessible_paper_rolls(rolls_grid)
    print(num_of_rolls)