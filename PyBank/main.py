# Imports the modules we need
import os
import csv

# Locates the CSV file used for analysis
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Creates the lists we can append the necessary info to
months = []
profitloss = []

# Holding variable at the start 
totalprofitloss = 0

# Reads the CSV file
with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skips the header
    csv_header = next(csv_file)

    # Loop through the data and append to the lists
    for row in csv_reader:
        months.append(row[0])
        profitloss.append(row[1])

        # Computes the total number of months in the dataset
        monthcount = len(months)
        
        # Adds to the initially empty variable totalprofitloss, and sums the total profit and loss
        totalprofitloss += int(row[1])

        







