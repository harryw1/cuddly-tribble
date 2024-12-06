import re

regex = r"mul\((\d+),(\d+)\)"
do_regex = r"do\(\)"
dont_regex = r"dont\(\)"

with open("input.txt", "r") as file:
    file_string = file.read()
    matches = re.finditer(regex, file_string, re.MULTILINE)

    total = 0
    calculate = True

    for matchNum, match in enumerate(matches, start=1):
        total += int(match.group(1)) * int(match.group(2))

    print(total)
