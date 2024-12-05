import csv


def check_safety(list_items):
    more_less_safety = True
    diff_safety = True
    problem_safety = True
    for i in range(len(list_items) - 1):
        var1 = int(list_items[i])
        var2 = int(list_items[i + 1])
        num_diff = abs(var1 - var2)
        if not problem_safety and not (num_diff >= 1 and num_diff <= 3):
            diff_safety = False
            return diff_safety
        if num_diff >= 1 and num_diff <= 3:
            continue
        else:
            problem_safety = False
            continue

    # Initial check of direction
    change_in_direction = 0
    decrement_or_increment = 'Decrease'  # Default is a decrement, or 0, increment is 1
    init_compare_1 = int(list_items[0])
    init_compare_2 = int(list_items[1])
    if init_compare_1 > init_compare_2:
        pass
    if init_compare_1 < init_compare_2:
        decrement_or_increment = 'Increase'

    for k in range(len(list_items) - 1):
        var1 = int(list_items[k])
        var2 = int(list_items[k + 1])
        if decrement_or_increment == 'Decrease' and (var2 > var1):
            change_in_direction = 1
            if problem_safety:
                problem_safety = False
                continue
            elif not problem_safety and change_in_direction == 1:
                more_less_safety = False
                print(
                    f'We are in more_less_safety: {more_less_safety} and change_in_direction: {change_in_direction}'
                )
                return more_less_safety
        if decrement_or_increment == 'Increase' and (var2 < var1):
            change_in_direction = 1
            if problem_safety:
                problem_safety = False
                continue
            elif not problem_safety and change_in_direction == 1:
                more_less_safety = False
                return more_less_safety

    return True


with open('input.csv', 'r') as input_file:
    input_text = csv.reader(input_file, delimiter=' ')
    counter = 0
    for row in input_text:
        temp_row = []
        for item in row:
            temp_row.append(int(item))
        if check_safety(temp_row):
            counter += 1

    print(f'Number of safe reports: {counter}')
