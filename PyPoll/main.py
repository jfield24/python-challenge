# Imports the modules we need
import os
import csv

# Forces python to change to directory with this python script
os.chdir(os.path.dirname(__file__))

# Locates the CSV file used for analysis
csvpath = os.path.join("Resources", "election_data.csv")

# Creates the lists we can append the necessary info to

votes = []
candidatenames = []


votespercandidate = [0, 0, 0, 0]

# Reads the CSV file
with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skips the header
    csv_header = next(csv_file)

    # Loop through the data and append to the votes list
    for row in csv_reader:
        votes.append(row[0])

        totalvotes = len(votes)

        candidatename = row[2]

        if candidatename not in candidatenames:
            candidatenames.append(candidatename)

        if candidatename == candidatenames[0]:
            votespercandidate[0] += 1

        elif candidatename == candidatenames[1]:
            votespercandidate[1] += 1

        elif candidatename == candidatenames[2]:
            votespercandidate[2] += 1
        
        elif candidatename == candidatenames[3]:
            votespercandidate[3] += 1

percent = [0, 0, 0, 0]

percent[0] = "{:.3%}".format(votespercandidate[0]/totalvotes)

percent[1] = "{:.3%}".format(votespercandidate[1]/totalvotes)

percent[2] = "{:.3%}".format(votespercandidate[2]/totalvotes)

percent[3] = "{:.3%}".format(votespercandidate[3]/totalvotes)


mostvotes = max(votespercandidate)
winner = candidatenames[(votespercandidate.index(mostvotes))]

votetotal = "{:,}".format(totalvotes)

candvotes0 = "{:,}".format(votespercandidate[0])
candvotes1 = "{:,}".format(votespercandidate[1])
candvotes2 = "{:,}".format(votespercandidate[2])
candvotes3 = "{:,}".format(votespercandidate[3])

print("Election Results")
print("--------------------")
print(f'Total Votes: {votetotal}')
print("--------------------")
print(f'{candidatenames[0]}: {percent[0]} ({candvotes0})')
print(f'{candidatenames[1]}: {percent[1]} ({candvotes1})')
print(f'{candidatenames[2]}: {percent[2]} ({candvotes2})')
print(f'{candidatenames[3]}: {percent[3]} ({candvotes3})')
print("--------------------")
print(f'Winner: {winner}')
print("--------------------")

# Exports text file with results
resultsfile = os.path.join("Analysis", "results.txt")

with open (resultsfile, "w") as textfile:
    textfile.write("Election Restults\n")
    textfile.write("--------------------\n")
    textfile.write(f'Total Votes: {votetotal}\n')
    textfile.write("--------------------\n")
    textfile.write(f'{candidatenames[0]}: {percent[0]} ({candvotes0})\n')
    textfile.write(f'{candidatenames[1]}: {percent[1]} ({candvotes1})\n')
    textfile.write(f'{candidatenames[2]}: {percent[2]} ({candvotes2})\n')
    textfile.write(f'{candidatenames[3]}: {percent[3]} ({candvotes3})\n')
    