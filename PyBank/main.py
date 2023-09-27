import os
import csv

# Set path for file
csvpath = os.path.join('Pybank', 'Resources.csv')
Outputpath = os.path.join('Pybank', 'Analysis')

# Open and read CSV
with open(csvpath) as csvfile:
    csv_reader = csv.reader (csvfile, delimiter=',')

    # Header
    csv_header = next(csv_reader)
    print("Financial Analysis")
    print("............................................................")

    # Loop through excel file
    months = []
    ColumnB = []
    for row in csv_reader:
        months.append(row[0])
        ColumnB.append(int(row[1]))

    # Sum of months
        SumMonths = len(months)
    print("Total Months: " + str(SumMonths))

    # Total calculation
    OverallChange = []
    for x in range(1, len(ColumnB)):
        OverallChange.append((int(ColumnB[x]) - int(ColumnB[x-1])))
    print("Total: " + "$" + str(sum(ColumnB)))
    # print("Average change: " + "$" + str(OverallChange))

    # Greatest increase calculation
    GreatestIncrease = max(OverallChange)
    print("Greatest increase in profits: " + str(months[OverallChange.index(max(OverallChange))+1]) + " " + "$" + str(GreatestIncrease))

    # Greatest decrease calculatin
    GreatestDecrease = min(OverallChange)
    print("Greatest decrease in profits: " + str(months[OverallChange.index(min(OverallChange))+1]) + " " + "$" + str(GreatestDecrease))

    # output to a text file
with open(Outputpath, "w") as FinalTextFile:
    FinalTextFile.write(
        "Financial Analysis\n"
        "............................................................\n"
        "Total Months: " + (str(SumMonths)) + ('\n')
        )