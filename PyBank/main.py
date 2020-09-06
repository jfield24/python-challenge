import os
import csv

csvpath = os.path.join(".", "Resources", "budget_data.csv")

totalmonths = []
totalprofitloss = []

monthcount = 0

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    print(f"Header:{csv_header}")

    for row in csv_reader:
        totalmonths.append(row[0])
        totalprofitloss.append(row[1])





