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
        for i in range(lb, db):
            ...

