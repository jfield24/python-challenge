# Imports the modules we need
import os
import csv

# Locates the CSV file used for analysis
csvpath = os.path.join("Resources", "budget_data.csv")

# Creates the lists we can append the necessary info to
months = []
profitloss = []
monthlychanges = []

# Sets an initial i value for use when looping
i = 0

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

        # Can format total profit/loss as a currency, adds a thousands separator 
        totalprofitloss = "${:,}".format(totalprofitloss)
        
        # We are going to add 1 to i for each iteration
        i += 1
        
        closingprofitloss = int(row[1])

        # If it is the first row being iterated then set openingprofitloss as closingprofitandloss
        if i == 1:

            openingprofitloss = closingprofitloss

        # If that isn't the case, then..
        else: 
            # Compute monthly change in profit/loss
            monthlychange = closingprofitloss - openingprofitloss

            # Append this value to the list of monthly change
            monthlychanges.append(monthlychange)

            # Makes the closingprofitloss the openingprofitloss for the next for loop
            openingprofitloss = closingprofitloss

    # Calculated the average monthly change
    averagemonthlychange = sum(monthlychanges)/(i - 1)

    # Format average monthly change as currency and add separator for thousands and cents
    averagemonthlychange = "${:,.2f}".format(averagemonthlychange)

    # Find the greatest increase in profits/losses over the entire period and respective month
    greatestincrease = max(monthlychanges)
    bestmonth = months[(monthlychanges.index(greatestincrease))+1]

    # Convert greatest increase to currency
    greatestincrease = "${:,}".format(greatestincrease)

    # Find the greatest decrease in profits/losses over the entire period and respective month
    greatestdecrease = min(monthlychanges)
    worstmonth = months[(monthlychanges.index(greatestdecrease))+1]

    # Convert greatest decrease to currency
    greatestdecrease = "${:,}".format(greatestdecrease)

   
# Prints my analysis to the terminal

print("Financial Analysis")
print("--------------------")
print(f'Total Months: {totalmonths}')
print(f'Total: {totalprofitloss}')
print(f'Average Change: {averagemonthlychange}')
print(f'Greatest Increase in Profits: {bestmonth} ({greatestincrease})')
print(f'Greatest Decrease in Profits: {worstmonth} ({greatestdecrease})')

# Exports text file with results
resultsfile = os.path.join("Analysis", )