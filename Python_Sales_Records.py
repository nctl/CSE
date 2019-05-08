import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    for row in reader:
        category = row[2]
        profit = row[13]
        if category == "Fruits":
            print(profit)
