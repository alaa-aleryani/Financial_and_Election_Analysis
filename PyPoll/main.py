import os
import csv

# To whoever going try this, change the file path to yours.
my_path = "C://Users/alaa3/Desktop/Python-Challenge/PyPoll"
csvpath = os.path.join(my_path, "Resources", "election_data.csv")
output_path = os.path.join(my_path, "Analysis", "election_data_analysis.txt")


# Creating lists
candidates_list = []

# Initializing the values
total_votes = 0
vote_count1 = 0
vote_count2 = 0
vote_count3 = 0
vote_percentage1 = 0
vote_percentage2 = 0
vote_percentage3 = 0
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

# The total number of votes each candidate won        
        if candidates_list[0] == candidate:
            vote_count1 +=1
        elif candidates_list[1] == candidate:
            vote_count2 +=1
        elif candidates_list[2] == candidate:
            vote_count3 +=1
    
# The percentage of votes each candidate won 
    vote_percentage1 = round((vote_count1/total_votes)*100, 3)
    vote_percentage2 = round((vote_count2/total_votes)*100, 3)
    vote_percentage3 = round((vote_count3/total_votes)*100, 3)  


# The winner of the election based on popular vote
# Since I knew by taking the length of the candidates_list 
# that I have just 3 candidates, (if elif) statements were easy to do.
# But if I had more candidates, creating a dictionary would be easier
# and more efficient, which is shown in "poll_script_2.py"
    if (vote_count1 > vote_count2) and (vote_count1 > vote_count3):
        winner = candidates_list[0]
    elif (vote_count2 > vote_count1) and (vote_count2 > vote_count3):
        winner = candidates_list[1]
    else:
        winner = candidates_list[2]

# Printing the analysis to the terminal:
election_data_results = (
 f' Elction Results'
 f'\n -------------------------------------------------- '   
 f'\n Total Votes: {total_votes}'
 f'\n -------------------------------------------------- '
 f'\n {candidates_list[0]}: {vote_percentage1}% ({vote_count1}) '
 f'\n {candidates_list[1]}: {vote_percentage2}% ({vote_count2})'
 f'\n {candidates_list[2]}: {vote_percentage3}% ({vote_count3})'
 f'\n -------------------------------------------------- '
 f'\n Winner: {winner}'
 f'\n -------------------------------------------------- '
)

print(election_data_results)

# Exporting a text file with the results:
with open(output_path, 'w') as datafile:
    datafile.write(election_data_results)
