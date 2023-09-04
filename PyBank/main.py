# First we'll import the os module to allow us to create file paths across operating systems 
# and csv module for reading CSV files
import os
import csv

# Creating paths
csvpath = os.path.join("C://Users/alaa3/Desktop/Python-Challenge/PyBank","Resources", "budget_data.csv")
output_path = os.path.join("C://Users/alaa3/Desktop/Python-Challenge/PyBank","Analysis","budget_data_analysis.txt")

# Initializing the values
total_amount = 0
total_months = 0
changes = 0
greatest_increase = 0
greatest_decrease = 0
price_changes = 0
greatest_increase_month = ''
greatest_decrease_month = ''


# Opening the file and reading it
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)      # This will skip the first row - the header!
    first_row = next(csvreader)       # This will skip the 1st actual row and store in the given variable
    total_months += 1                 # adding 1 to the length of months b/c we skipped the 1st actual row.
    total_amount += int(first_row[1]) # will change the initial amount from 0 to the 1st price occurance.
    prev_amount = int(first_row[1])   # storing the first price in this variable

    for row in csvreader:             # looping through the rows of the sheet.

#The total number of months included in the dataset 
        total_months += 1
    
#The net total amount of "Profit/Losses" over the entire period
        total_amount += int(row[1])

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#the average of all b2# - b1#
        current_amount = int(row[1])
        changes = current_amount - prev_amount
        price_changes += changes
        average_change = round(price_changes / (total_months - 1), 2)        

#The greatest increase in profits (date and amount) over the entire period 
        if changes > greatest_increase:
            greatest_increase = changes
            greatest_increase_month = row[0]
            monthDAY_greatest_increase = greatest_increase_month.split("-")

#The greatest decrease in profits (date and amount) over the entire period
        elif changes < greatest_decrease:
            greatest_decrease = changes
            greatest_decrease_month = row[0]
            monthDAY_greatest_decrease = greatest_decrease_month.split("-")
        prev_amount = current_amount    


# Printing the analysis to the terminal:
budget_data_results = (
 f' --------------------------------------------------'   # \n inserting new lines
 f'\n Financial Analysis'
 f'\n -------------------------------------------------- '   
 f'\n Total Months: {total_months}'
 f'\n Total: ${total_amount}'
 f'\n Average Change: ${average_change}'
 f'\n Greatest Increase in Profits: {monthDAY_greatest_increase[1]}-{monthDAY_greatest_increase[0]} $({greatest_increase})'
 f'\n Greatest Decrease in Profits: {monthDAY_greatest_decrease[1]}-{monthDAY_greatest_decrease[0]} $({greatest_decrease})'
)

print(budget_data_results)

# Exporting a text file with the results:
with open(output_path, 'w') as datafile:
    datafile.write(budget_data_results)