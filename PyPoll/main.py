# HOMEWORK MODULE 03 - PYPOLL

# Importing the "os" module - to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Store the CSV file path in a variable called filepath
filepath = os.path.join('Resources','election_data.csv')

# Creating lists to add the csv values to
ballots_id = []
candidates = []
candidates_list = []
candidate_row =[]
perc_per_candidate = []
votes_per_candidate = []

# Reading using CSV module
with open(filepath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row, so the code will skip the header row
    header = next(csvreader)

    # Counting total votes
    for row in csvreader:
       ballots_id.append(row[0])
       candidate_row.append(row[2])
    total_votes = len(ballots_id)

    #Creating a list of unique candidates who received votes
    for i in range (0,total_votes):
        var_candidate = candidate_row[i]
        candidates.append(var_candidate)
        if var_candidate not in candidates_list:
          candidates_list.append(var_candidate)
    #Couting total of candidates   
    total_candidates = len(candidates_list)   

    #Counting votes per candidate
    for j in range (0,total_candidates):
        name = candidates_list[j]
        votes_per_candidate.append(candidate_row.count(name))
        var_perc_candidate = votes_per_candidate[j]/total_votes
        perc_per_candidate.append(var_perc_candidate)

    #And the winner is:
    winner = votes_per_candidate.index(max(votes_per_candidate))
    
    # Printing results in the terminal

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes:}")
    print("----------------------------")
    for k in range (0,total_candidates): 
        print(f"{candidates_list[k]}: {perc_per_candidate[k]:.3%} ({votes_per_candidate[k]:})")
    print("----------------------------")
    print(f"Winner: {candidates_list[winner]}")
    print("----------------------------")

    #EXPORTING THE RESULTS TO A TEXT FILE

    resultspath = os.path.join('analysis','results_pypoll.txt')

    with open(resultspath,"w") as results:
    
        results.write("Election Results\n")
        results.write("----------------------------\n")
        results.write(f"Total Votes: {total_votes:}\n")
        results.write("----------------------------\n")
        for k in range (0,total_candidates): 
            results.write(f"{candidates_list[k]}: {perc_per_candidate[k]:.3%} ({votes_per_candidate[k]:})\n")
        results.write("----------------------------\n")
        results.write(f"Winner: {candidates_list[winner]}\n")
        results.write("----------------------------")