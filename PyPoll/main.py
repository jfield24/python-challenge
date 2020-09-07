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


print(totalvotes)
print(candidatenames)
print(f'({votespercandidate})')