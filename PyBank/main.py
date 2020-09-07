# Imports the modules we need
import os
import csv

# Locates the CSV file used for analysis
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Creates the lists we can append the necessary info to
months = []
profitloss = []
monthlychanges = []

# Holding variable at the start 
totalprofitloss = 0
monthcount = 0
openingprofitloss = 0
closingprofitloss = 0
monthlychange = 0

# Reads the CSV file
with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skips the header
    csv_header = next(csv_file)

    # Loop through the data and append to the lists
    for row in csv_reader:
        months.append(row[0])
        profitloss.append(int(row[1]))

        # Computes the total number of months in the dataset
        totalmonths = len(months)
        
        # Adds to the initially empty variable totalprofitloss, and sums the total profit and loss
        totalprofitloss = sum(profitloss)
    
        # Set an initial value of iterator
        i = 0

        
        for i in range(len(profitloss)-1):

            closingprofitloss = int(profitloss[i+1])
            openingprofitloss = int(profitloss[i])
            monthlychange = closingprofitloss - openingprofitloss

            monthlychanges.append(int(monthlychange))

        averagemonthlychange = (sum(monthlychanges))/int(totalmonths)

    print(averagemonthlychange)

            
            


        









