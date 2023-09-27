import os
import csv

# set path for file
csvpath = os.path.join('PyPoll', 'Resources.csv')

# add variable
TotalVotes = 0
CandidateVotes = {}
VotedCandidates = []

# candidate_index={0,1,2}

# TotalCandidats = 0
# CandidateVotes = 0
# Candidate1Total = 0
# Candidate2Total = 0
# Candidate3Total = 0

Candidates = []



# open and read csv
with open (csvpath) as csvfile:
    csv_reader = csv.reader (csvfile, delimiter=',')

    # Header
    csv_header = next(csv_reader)
    print ("Election Results")
    print("--------------------------------------")

    # loop through file
    for row in csv_reader:
        Candidates.append(row[2])
        Ballots = row
        TotalVotes =+1

    # sort candidates and find unique
SortedCandidates = sorted(Candidates)
for i in range(len(SortedCandidates)):
    if SortedCandidates[i]!= SortedCandidates[i-1]:
        VotedCandidates.append(SortedCandidates[i-1])

for Candidate in VotedCandidates:

        # loop to find sum for each candidate
    for i in range(len(Candidates)):
        if Candidates[i] ==Candidates:
            votes = votes+1
     # add votes per candidate
        CandidateVotes.append(votes)
        