import os
import csv

# Set path for file
csvpath = os.path.join('Pybank', 'Resources.csv')

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

    # # output to a text file
    # file = open("output.txt","w")
    # file.write("Financial Analysis" + "\n")
    # file.write("...................................................................................." + "\n")
    # file.write("total months: " + str(total_months) + "\n")
    # file.write("Total: " + "$" + str(sum(P)) + "\n")
    # file.write("Average change: " + "$" + str(revenue_average) + "\n")
    # file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")
    # file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")
    # file.close()
