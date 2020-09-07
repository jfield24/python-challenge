# Imports the modules we need
import os
import csv

# Locates the CSV file used for analysis
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Creates the lists we can append the necessary info to
months = []
profitloss = []
monthlychanges = []

# Sets the initial varaibles
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

        monthcount +=1
        
        closingprofitloss = int(row[1])

        if monthcount == 1:

            openingprofitloss = closingprofitloss

        else: 
            monthlychange = closingprofitloss - openingprofitloss

            monthlychanges.append(monthlychange)

            openingprofitloss = closingprofitloss

    averagemonthlychange = sum(monthlychanges)/(monthcount - 1)

    averagemonthlychange = round((averagemonthlychange),2)

    print(averagemonthlychange)




            



            
            


        









