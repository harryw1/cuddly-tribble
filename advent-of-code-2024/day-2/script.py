import csv


def check_diff_and_order(list_items):
    """Check if list has differences <= 3 and is strictly increasing or decreasing"""
    if len(list_items) <= 1:
        return True

    # Determine if sequence should be increasing or decreasing
    is_increasing = list_items[1] > list_items[0]

    for i in range(len(list_items) - 1):
        curr, next_val = list_items[i], list_items[i + 1]
        diff = abs(next_val - curr)

        # Check if difference is more than 3
        if diff > 3:
            return False

        # Check if order is maintained
        if is_increasing and next_val <= curr:
            return False
        if not is_increasing and next_val >= curr:
            return False

    return True


def try_removing_one(list_items):
    """Try removing one item to make the list safe"""
    for i in range(len(list_items)):
        # Create new list without item at index i
        new_list = list_items[:i] + list_items[i + 1 :]
        if check_diff_and_order(new_list):
            return True
    return False


def is_list_safe(list_items):
    """Main function to check if list is safe or can be made safe by removing one item"""
    # First check if list is already safe
    if check_diff_and_order(list_items):
        return True

    # If not safe, try removing one item
    return try_removing_one(list_items)


# Read and process input
with open("input.csv", "r") as input_file:
    input_text = csv.reader(input_file, delimiter=" ")
    counter = 0
    for row in input_text:
        temp_row = [int(item) for item in row]
        if is_list_safe(temp_row):
            counter += 1
            print(f"Safe list found: {temp_row}")

    print(f"Number of safe reports: {counter}")
