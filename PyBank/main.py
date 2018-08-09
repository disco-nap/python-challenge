#Your task is to create a Python script that analyzes the records to calculate each of the following:
import os
import csv

csvpath = os.path.join("..", "..", "budget_data.csv")


month = []
profit_losses = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)
    count = 0
    total = 0
    maximum = 0
    minimum = 0


    for row in csvreader:
        count = count + 1
        total = total + int(row[1])
        avg_change = (int(total)/int(count))
        if int(row[1]) > maximum:
            maximum = int(row[1])
            maxdate = row[0]
        if int(row[1]) < minimum:
            minimum = int(row[1])
            mindate = row[0]
        

print("Financial Analysis")
print("------------------------")
print(f'Total months: {count}')
print(f'Total: ${total:.2f}')
print(f'Average Change: ${avg_change:.2f}')
print(f'Greatest Increase in Profits: {maxdate} ${maximum:.2f}')
print(f'Greatest Decrease in Profits: {mindate} ${minimum:.2f}')







#The total number of months included in the dataset

#The total net amount of "Profit/Losses" over the entire period

#The average change in "Profit/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#As an example, your analysis should look similar to the one below:

#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.