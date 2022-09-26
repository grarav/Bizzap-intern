import csv
with open('my.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)