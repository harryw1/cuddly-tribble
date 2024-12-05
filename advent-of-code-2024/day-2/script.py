import csv


def check_safety(list_items):
    more_less_safety = True
    diff_safety = True
    for i in range(len(list_items)):
        for j in range(i + 1, len(list_items)):
            num_diff = abs(i - j)
            if num_diff >= 1 & num_diff <= 4:
                continue
            else:
                diff_safety = False
                return diff_safety
        for k in range(i + 1, len(list_items)):
            decrement_or_increment = 0  # Default is a decrement, or 0, increment is 1
            if i < k:
                continue
            if i > k:
                decrement_or_increment = 1
            for j in range(k + 1, len(list_items)):
                if decrement_or_increment == 0:
                    if k > j:
                        more_less_safety = False
                        return more_less_safety
                    else:
                        continue
                if decrement_or_increment == 1:
                    if k < j:
                        more_less_safety = False
                        return more_less_safety


with open("input.csv", "r") as input_file:
    input_text = csv.reader(input_file, delimiter=" ")
    for row in input_text:
        temp_row = []
        for item in row:
            temp_row.append(int(item))
        check_safety(temp_row)
