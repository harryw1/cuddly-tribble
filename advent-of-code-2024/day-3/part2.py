import re


def process_multiplications(text):
    start_pattern = r"do\(\)"
    multiply_pattern = r"mul\((\d+),(\d+)\)"
    stop_pattern = r"don't\(\)"

    # Keep track of whether we're in the multiplication zone and the running total
    in_multiply_zone = True
    total = 0

    # Function to handle multiplication for each match
    def multiply_match(match):
        nonlocal total
        if not in_multiply_zone:
            return match.group(0)  # Return unchanged if not in multiply zone
        # Extract both numbers and multiply them
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        result = num1 * num2
        total += result  # Add to running total
        return str(result)

    # Split the text into chunks based on patterns
    chunks = []
    current_pos = 0

    # Find all patterns in the text
    for match in re.finditer(f"({start_pattern})|({stop_pattern})", text):
        # Add the text before this pattern
        chunks.append(text[current_pos : match.start()])

        if match.group(1):  # Start pattern found
            in_multiply_zone = True
        elif match.group(2):  # Stop pattern found
            in_multiply_zone = False

        # Add the pattern itself
        chunks.append(match.group(0))
        current_pos = match.end()

    # Add any remaining text
    chunks.append(text[current_pos:])

    # Process each chunk
    result = ""
    in_multiply_zone = True

    for chunk in chunks:
        if re.match(start_pattern, chunk):
            in_multiply_zone = True
            result += chunk
        elif re.match(stop_pattern, chunk):
            in_multiply_zone = False
            result += chunk
        else:
            # Apply multiplication pattern only in multiply zone
            if in_multiply_zone:
                result += re.sub(
                    multiply_pattern, lambda m: multiply_match(m), chunk
                )
            else:
                result += chunk

    return result, total


with open("input.txt", "r") as file:
    file_string = file.read()
    result, total = process_multiplications(file_string)
    print("\nTotal of all multiplications in input file:", total)
