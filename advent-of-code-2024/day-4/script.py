# Part 1: Given some input that appears like
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# Find all instances of the word "XMAS" and
# return the number of times it appears
# vertically, horizontally, and diagonally.


def is_valid_position(data, i, j):
    return 0 <= i < len(data) and 0 <= j < len(data[0])


def horizontal(data):
    count = 0
    for line in data:
        count += line.count("XMAS")
    return count


def vertical(data):
    count = 0
    for i in range(len(data[0])):
        for j in range(len(data)):
            if data[j][i : i + 4] == "XMAS":
                count += 1
    return count


def diagonal(data):
    count = 0
    for i in range(len(data) - 3):
        for j in range(len(data[0]) - 3):
            if (
                data[i][j] == "X"
                and data[i + 1][j + 1] == "M"
                and data[i + 2][j + 2] == "A"
                and data[i + 3][j + 3] == "S"
            ):
                count += 1


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().split("\n")
    print(horizontal(data) + vertical(data) + diagonal(data))
