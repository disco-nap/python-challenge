import os
import csv

csvpath = os.path.join("..", "..", "budget_data.csv")

date = []
profitloss = []
profitlosschange = []

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
        profitloss.append(row[1])
        date.append(row[0])


for a, b in zip(profitloss, profitloss[1:]):
    profitlosschange.append(int(b) - int(a))

total_change = sum(profitlosschange)
avg_change = total_change / (int(count) -1)

for monthchange in profitlosschange:
    if int(monthchange) > maximum:
        maximum = int(monthchange)
    if int(monthchange) < minimum:
        minimum = int(monthchange)

print("Financial Analysis")
print("------------------------")
print(f'Total months: {count}')
print(f'Total: ${total:.2f}')
print(f'Average Change: ${avg_change:.2f}')
print(f'Greatest Increase in Profits: ${maximum:.2f}')
print(f'Greatest Decrease in Profits: ${minimum:.2f}')










# In addition, your final script should both print the analysis to the terminal and export a text file with the results.