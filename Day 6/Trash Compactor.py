import math


def file_to_list(filename = "input.txt"):
    with open(filename, "r") as file:
        # .strip() removes whitespace characters from both ends of the string
        content = [line.strip().split() for line in file.readlines() if line.strip()]
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

    prob = zip(*problems) # flipping the matrix - Transpose of the matrix (to iterate the columns as rows)
    total_result = 0

    for number in prob:
        result = do_operation(number[:-1], number[-1]) # separating the numbers and the operator
        total_result += result

    print(total_result)