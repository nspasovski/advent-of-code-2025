import math
from itertools import zip_longest


def file_to_list(filename = "input.txt"):
    with open(filename, "r") as file:
        # .strip() removes whitespace characters from both ends of the string
        content = [list(line.strip('\n')) for line in file.readlines() if line.strip()]
    return content


def do_operation(numbers_row, operator):
    numbers_row = map(int, numbers_row)
    result_row = 0

    if operator == "+":
       result_row = sum(numbers_row)
    elif operator == "*":
        result_row = math.prod(numbers_row)

    return result_row


if __name__ == '__main__':
    problems = file_to_list()

    numbers_list = list(zip_longest(*problems[:-1], fillvalue=' '))
    operators = "".join(problems[-1]).split()

    num_by_columns = [] # list of sets of columns
    column = []
    total_result = 0

    for num in numbers_list:
        number = "".join(num).strip(' ')

        if len(number) == 0: # if we reach the empty column
            num_by_columns.append(column) # add to list the set of numbers by columns
            column = [] # reset the column
        else:
            column.append(number)

    num_by_columns .append(column) # adding the last set of numbers

    for num, op in zip(num_by_columns, operators):
        total_result += do_operation(num, op)
        # for testing purposes we can print the return value from do_operation

    print(f'Final res = {total_result}')
