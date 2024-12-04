import csv
from unittest.mock import right

with open('input.csv', 'r') as input_file:
    input_string = csv.reader(input_file, delimiter=' ')
    col_a = []
    col_b = []
    for line in input_string:
        col_a.append(line[0])
        col_b.append(line[3])


    col_a.sort()
    col_b.sort()

    distances = []

    for i in range(len(col_a)):
        distances.append(abs((int(col_a[i]) - int(col_b[i]))))


    # print(sum(distances))
    a = [int(item) for item in col_a]
    b = [int(item) for item in col_b]

    sim_score = 0

    for i in range(len(a)):
        b.count(a[i])
        sim_score += (a[i] * b.count(a[i]))

    print(sim_score)
