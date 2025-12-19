def file_to_list(filename = "input.txt"):
    with open(filename, "r") as file:
        # .strip() removes whitespace characters from both ends of the string
        content = [line.strip() for line in file.readlines() if line.strip()]
    return content

# greedy algorithm + constrained sliding window technique

def find_largest_joltage(bat):
    list_power = list(map(int, bat))

    max_power = 0
    skips_remaining = len(list_power) - 12 # buffer size

    i = 0
    while i < len(list_power) - skips_remaining:
        current_cell = list_power[i]
        move_index = 0

        # trying to find the highest digit with the skips remaining
        for skip in range(1, skips_remaining + 1): # adding 1 to include the stop value in the range
            if i + skip >= len(list_power):
                break

            next_cell = list_power[i + skip]

            if next_cell > current_cell:
                current_cell = next_cell
                move_index = skip

        # skip 'move_index' positions, add 1 to start from the next unvisited index
        i += move_index + 1

        # reduce the sliding window size for the skipped positions
        if skips_remaining - move_index >= 0:
            skips_remaining -= move_index

        # adding up the max power (building the number with each iteration of digits)
        max_power = max_power * 10 + current_cell

    return max_power

if __name__ == '__main__':
    batteries = file_to_list()
    total_output_joltage = 0

    for battery in batteries:
        battery_joltage = find_largest_joltage(battery)
        total_output_joltage += battery_joltage

    print(total_output_joltage)

