import os
import csv

# set path for file
csvpath = os.path.join('PyPoll', 'Resources.csv')

# open and read csv
with open (csvpath) as csvfile:
    csv_reader = csv.reader (csvfile, delimiter=',')

    # Header
    csv_header = next(csv_reader)
    print ("Election Results")
    print("--------------------------------------")

    # Loop through excel file

    Votes = []
    for row in csv_reader:
        Votes.append(row[0])

    # Sum of votes
        TotalVotes = len(Votes)
    print("Total Votes: " + str(TotalVotes))
    print("--------------------------------------")

    # Percentage of votes each candidate won - Mister Stockham
