                                    #################### Using Dictionaries ####################

import os
import csv

# To whoever going try this, change the file path to yours!
my_path = "C://Users/alaa3/Desktop/Python-Challenge/PyPoll"
csvpath = os.path.join(my_path, "Resources", "election_data.csv")
output_path = os.path.join(my_path, "Analysis", "election_data_analysis.txt")


# Creating lists
candidates_list = [] # Initializing a list
candidate_votes = {} # Initializing a dictionary
output_votes = []    # Initializing a list

# Initializing the values
total_votes = 0
winner = ''


# Opening the file and reading it
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# This will skip the 1st row and store the values in the variable given
    electionDATA_header = next(csvreader)  

# Looping through each row in the worksheet
    for row in csvreader:

# The total number of votes cast
        total_votes += 1

# A complete list of candidates who received votes
        candidate = row[2] # To make it easy to read
        if candidate not in candidates_list:
            candidates_list.append(candidate)
####################################################################################
            candidate_votes[candidate] = 0 # setting the dictionary key to be the candidates' names.
        candidate_votes[candidate] += 1 # Adding 1 vote to the candidate whenever a candidates name appears.
            

    winner_votes = 0 # Initialzing the winner votes to 0 so we compare each candidates votes

    for candidate in candidate_votes:
        # The total number of votes each candidate won
        votes = candidate_votes[candidate]
        # The percentage of votes each candidate won 
        vote_percentage = round((votes/total_votes)*100, 3)  
        # This list is to be used later when printing and exporting the results
        output_votes.append(f'{candidate}: {vote_percentage}% ({votes}) ')
        # The winner of the election based on popular vote
        if votes > winner_votes:
            winner_votes = votes
            winner = candidate


# Printing the analysis to the terminal:
election_data_results = (
 f' Election Results'
 f'\n -------------------------------------------------- '   
 f'\n Total Votes: {total_votes}'
 f'\n -------------------------------------------------- '
 f'\n {output_votes[0]}' 
 f'\n {output_votes[1]}'  
  f'\n {output_votes[2]}' 
 f'\n -------------------------------------------------- '
 f'\n Winner: {winner}'
 f'\n -------------------------------------------------- '
)

print(election_data_results)

# Exporting a text file with the results:
with open(output_path, 'w') as datafile:
    datafile.write(election_data_results)