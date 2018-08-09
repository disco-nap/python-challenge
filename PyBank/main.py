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

    for row in csvreader:
        count = count + 1
        total = total + int(row[1])
        profitloss.append(row[1])
        date.append(row[0])


for a, b in zip(profitloss, profitloss[1:]):
    profitlosschange.append(int(b) - int(a))

total_change = sum(profitlosschange)
avg_change = total_change / (int(count) -1)

maximum = max(profitlosschange)
minimum = min(profitlosschange)

max_index = profitlosschange.index(maximum)
min_index = profitlosschange.index(minimum)

max_date = date[max_index + 1]
min_date = date[min_index + 1]


print("Financial Analysis")
print("------------------------")
print(f'Total months: {count}')
print(f'Total: ${total:.2f}')
print(f'Average Change: ${avg_change:.2f}')
print(f'Greatest Increase in Profits: {max_date} ${maximum:.2f}')
print(f'Greatest Decrease in Profits: {min_date} ${minimum:.2f}')










# In addition, your final script should both print the analysis to the terminal and export a text file with the results.