import os
import csv

csvpath = os.path.join("..", "..", "election_data.csv")


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)

    vote_count = 0
    candidates = []
    candidate1count = 0
    candidate2count = 0
    candidate3count = 0
    candidate4count = 0

    for row in csvreader:
        vote_count = vote_count + 1
        if row[2] not in candidates:
            candidates.append(row[2])               
        if row[2] == candidates[0]:
            candidate1count = candidate1count + 1
        elif row[2] == candidates[1]:
            candidate2count = candidate2count + 1
        elif row[2] == candidates[2]:
            candidate3count = candidate3count + 1
        elif row[2] == candidates[3]:
            candidate4count = candidate4count + 1

candidate1percent = (candidate1count / vote_count) * 100
candidate2percent = (candidate2count / vote_count) * 100
candidate3percent = (candidate3count / vote_count) * 100
candidate4percent = (candidate4count / vote_count) * 100
            
if candidate1percent > candidate2percent and candidate1percent > candidate3percent and candidate1percent > candidate4percent:
    winner = candidates[0]
elif candidate2percent > candidate1percent and candidate2percent > candidate3percent and candidate2percent > candidate4percent:
    winner = candidates[1]
elif candidate3percent > candidate1percent and candidate3percent > candidate2percent and candidate3percent > candidate4percent:
    winner = candidates[2]
elif candidate4percent > candidate1percent and candidate4percent > candidate2percent and candidate4percent > candidate3percent:
    winner = candidates[3]


print("Election Results")
print("-----------------------")
print(f'Total Votes: {vote_count}')
print("-----------------------")
print(f'{candidates[0]}: {candidate1percent:.2f}% ({candidate1count})')
print(f'{candidates[1]}: {candidate2percent:.2f}% ({candidate2count})')
print(f'{candidates[2]}: {candidate3percent:.2f}% ({candidate3count})')
print(f'{candidates[3]}: {candidate4percent:.2f}% ({candidate4count})')
print("-----------------------")
print(f'Winner: {winner}')
print("-----------------------")


#In addition, your final script should both print the analysis to the terminal and export a text file with the results.



