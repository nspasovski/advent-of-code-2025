def file_to_list(filename = "input.txt"):
    with open(filename, "r") as file:
        # input given in one line
        content = file.readline().split(',')
    return content


def repeating_sub_string(s, l, counter, index = 0):
    next_index = index + counter

    if index + counter >= l: # if substrings reach the end, we have repeating sequence
        return True

    # checking 2 consecutive substrings for equality, ex. str[0:2] == str[2:4], substrings of length 2
    if s[index:next_index] == s[next_index: next_index + counter]:
        return repeating_sub_string(s, l, counter, index + counter)

    return False


def is_invalid(s, l):
    for size in range(1, l//2 + 1):
        # check if we can generate sub strings of len size(in len of 5, we can't have sub strings on len 3), if so, check if it repeats itself
        if l % size == 0 and repeating_sub_string(s, l, size):
            return True
    return False


if __name__ == '__main__':
    ranges = file_to_list()

    sum_ids = 0
    for r in ranges:
        lb, db = map(int, r.split('-'))
        for i in range(lb, db+1):
            s = str(i)
            l = len(s)
            if is_invalid(s, l):
                sum_ids += i
                # print(f'invalid ID {i}')

    print(f'Sum of all invalid IDs = {sum_ids}')
