import os
import csv

csvpath = os.path.join("..", "..", "budget_data.csv")

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


# In addition, your final script should both print the analysis to the terminal and export a text file with the results.