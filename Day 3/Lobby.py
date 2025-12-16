def file_to_list(filename = "input.txt"):
    with open(filename, "r") as file:
        # .strip() removes whitespace characters from both ends of the string
        content = [line.strip() for line in file.readlines() if line.strip()]
    return content

def find_largest_joltage(bat):
    list_power = list(map(int, bat))

    max_left_digit = 0
    left_index = 0
    # first we find the largest digit and it's index (this cannot be the last digit)
    for i, p in enumerate(list_power[:-1]):
        if p > max_left_digit:
            max_left_digit = p
            left_index = i

    max_right_digit = 0
    # now we find the largest digit starting from the first one's position
    for j, pr in enumerate(list_power[left_index + 1:]):
        if pr > max_right_digit:
            max_right_digit = pr

    max_power = max_left_digit * 10 + max_right_digit

    return max_power

if __name__ == '__main__':
    batteries = file_to_list()
    total_output_joltage = 0

    for battery in batteries:
        battery_joltage = find_largest_joltage(battery)
        total_output_joltage += battery_joltage

    print(total_output_joltage)
