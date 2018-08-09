#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

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
        for candidate in candidates:
            if candidate == candidates[0]:
                candidate1count = candidate1count + 1
            if candidate == candidates[1]:
                candidate2count = candidate2count + 1
            if candidate == candidates[2]:
                candidate3count = candidate3count + 1
            if candidate == candidates[3]:
                candidate4count = candidate4count + 1

candidate1percent = candidate1count / vote_count
candidate2percent = candidate2count / vote_count
candidate3percent = candidate3count / vote_count
candidate4percent = candidate4count / vote_count
            
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
print(f'{candidates[0]}: {candidate1percent}% ({candidate1count})')
print(f'{candidates[1]}: {candidate2percent}% ({candidate2count})')
print(f'{candidates[2]}: {candidate3percent}% ({candidate3count})')
print(f'{candidates[3]}: {candidate4percent}% ({candidate4count})')
print("-----------------------")
print(f'Winner: {winner}')





#The total number of votes cast

#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.


#As an example, your analysis should look similar to the one below:


#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#   -------------------------

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.



