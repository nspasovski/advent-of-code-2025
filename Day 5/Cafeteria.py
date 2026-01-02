def file_to_list(filename = "input.txt"):
    with open(filename, "r") as file:
        # read the entire file into single string, strip the outer whitespaces, separate by the empty line - \n\n
        sections = file.read().strip().split("\n\n")

        # Section 0 is ranges, Section 1 is IDs
        ranges_list = sections[0].splitlines()
        ids_list = sections[1].splitlines()

        ranges = [list(map(int, r.split('-'))) for r in ranges_list]
        ids = [int(i) for i in ids_list]

    return ranges, ids



if __name__ == '__main__':
    ranges, ids = file_to_list()

    # sorting for better search
    ranges.sort()
    ids.sort()

    num_fresh_ingredients = 0

    for ingredient_id in ids:
        for r1, r2 in ranges:

            if r1 <= ingredient_id <= r2:
                num_fresh_ingredients += 1
                # print(f'good ingredient {ingredient_id} in range {r1} -> {r2}')
                break

            # if the id is smaller than the starting range (in already sorted list), then we break to prevent unnecessary checks
            if ingredient_id < r1:
                break

    print(num_fresh_ingredients)
