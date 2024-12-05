import csv


def diff_safety(list_items):
    diff_safety = True
    for i in range(len(list_items) - 1):
        var1 = int(list_items[i])
        var2 = int(list_items[i + 1])
        num_diff = abs(var1 - var2)
        if num_diff >= 1 and num_diff <= 3:
            continue
        else:
            return not diff_safety
    return diff_safety


def more_less_safety(list_items):
    more_less_safety = True
    decrement_or_increment = (
        "Decrease"  # Default is a decrement, or 0, increment is 1
    )
    print(f"List of items {list_items}")
    init_compare_1 = int(list_items[0])
    init_compare_2 = int(list_items[1])
    if init_compare_1 > init_compare_2:
        pass
    if init_compare_1 < init_compare_2:
        decrement_or_increment = "Increase"

    for k in range(len(list_items) - 1):
        var1 = int(list_items[k])
        var2 = int(list_items[k + 1])
        if decrement_or_increment == "Decrease" and (var2 > var1):
            return not more_less_safety
        if decrement_or_increment == "Increase" and (var2 < var1):
            return not more_less_safety

    return more_less_safety


def slice_except_one(list_items):
    safety = True
    temp_row = []
    for i in range(len(list_items)):
        temp_safety = True
        temp_row.append(list_items[:i] + list_items[i + 1 :])
        temp_safety = diff_safety(temp_row)
        if not temp_safety:
            return False
        temp_safety = more_less_safety(temp_row)
        if not temp_safety:
            return False
    return safety


def check_safety(list_items):
    check_1 = diff_safety(list_items)
    if not check_1:
        check_1 = slice_except_one(list_items)
    check_2 = more_less_safety(list_items)
    if not check_2:
        check_2 = slice_except_one(list_items)

    if check_1 and check_2:
        return True
    else:
        return False


with open("input.csv", "r") as input_file:
    input_text = csv.reader(input_file, delimiter=" ")
    counter = 0
    for row in input_text:
        temp_row = []
        for item in row:
            temp_row.append(int(item))
        if check_safety(temp_row):
            counter += 1
            print(temp_row, check_safety(temp_row))

    print(f"Number of safe reports: {counter}")
