def file_to_list(filename = "input.txt"):
    with open(filename, "r") as file:
        # read the entire file into single string, strip the outer whitespaces, separate by the empty line - \n\n
        sections = file.read().strip().split("\n\n")

        # Section 0 is ranges, Section 1 is IDs
        ranges_list = sections[0].splitlines()

        ranges = [list(map(int, r.split('-'))) for r in ranges_list]

    return ranges



if __name__ == '__main__':
    ranges = file_to_list()
    # sorting for better search
    ranges.sort()

    num_fresh_ingredients = 0

    merged_ranges = []
    prev_r1 = prev_r2 = 0

    for r1, r2 in ranges:
        if prev_r1 <= r1 <= prev_r2:
            prev_r2 = max(prev_r2, r2) # if the current range is between the previous one, max gets the higher value

            if merged_ranges:
                merged_ranges[-1][1] = prev_r2
        else:
            merged_ranges.append([r1, r2])
            prev_r1 = r1
            prev_r2 = r2


    for r1, r2 in merged_ranges:
        num_fresh_ingredients += r2 - r1 + 1 # adding one to include the border range ID

    print(num_fresh_ingredients)
