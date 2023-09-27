import os
import csv

# set path for file
csvpath = os.path.join('PyPoll', 'Resources.csv')
Outputpath = os.path.join('PyPoll', 'Analysis')

# set variables
WinningCount = 0
TotalVotes = 0
WinningPercentage = 0
WinningCandidate = ""

# set lists
CandidateVotesdict = {}
Votes = []
VotedCandidatesList = []

# open and read csv
with open (csvpath) as csvfile:
    csv_reader = csv.reader (csvfile, delimiter=',')

    # Header
    csv_header = next(csv_reader)
    print ("Election Results")
    print("--------------------------------------")
    
    # loop through file
    for row in csv_reader:
        Votes.append(row[0])
        SumVotes = len(Votes)

        # assign columns (candidate names)
        ColumnNames = row[2]
        TotalVotes +=1
    
        # Assign conditionals for candidates
        if ColumnNames in CandidateVotesdict:
            # VotedCandidatesList.append(ColumnNames)

            # Set the count with dictionary, at 0 and add each vote
            CandidateVotesdict[ColumnNames] +=1
        else:
            CandidateVotesdict[ColumnNames] = 1

    # print and transfer to Analysis
    print ('Total Votes: ' + str(SumVotes))

    # New loop for candidate list
    for ColumnNames in CandidateVotesdict:
        Votes = CandidateVotesdict[ColumnNames]

        # percentage
        VotePercentage = float(float(Votes) / float(SumVotes)) * 100

        # print and transfer to Analysis
        print(f'{ColumnNames}: {VotePercentage:.1f}% ({Votes:,})')

        # Determine winning count with boolean
        if (Votes > WinningCount) and (VotePercentage > WinningPercentage):
            WinningCount = Votes
            WinningPercentage = VotePercentage
            # winner
            Winner = ColumnNames
            # print(Winner)

# Transfer to Analysis
with open(Outputpath, "w") as FinalTextFile:
    FinalTextFile.write(
        "Election Results\n"
        "--------------------------------------\n"
        )