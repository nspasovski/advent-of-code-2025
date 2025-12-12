def file_to_list(filename = "input.txt"):
    with open(filename, "r") as file:
        # input given in one line
        content = file.readline().split(',')
    return content

if __name__ == '__main__':
    ranges = file_to_list()

    sum_ids = 0
    for r in ranges:
        lb, db = map(int, r.split('-'))
        for i in range(lb, db+1):
            s = str(i)
            l = len(s)
            if l % 2 == 0:
                if s[:l//2] == s[l//2:]:
                    sum_ids += i
                    # print(f'Invalid ID {i}')

    print(f'Sum of all invalid IDs = {sum_ids}')

# can be improved if we only iterate half of the number and check if it repeats, ex. 1111-2222, 11-22 => 11 11 and 22 22