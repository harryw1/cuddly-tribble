import csv
import os

def test():
    with open('test.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['a', 'b', 'c'])
        writer.writerow(['1', '2', '3'])

    with open('test.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

    os.remove('test.csv')

test()
