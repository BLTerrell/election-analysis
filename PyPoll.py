# The data we need to have and deliver to audit the election
# 1) Total # of votes in the election
# 2) List of candidates that received votes
# 3) Total # of votes per candidate
# 4) Percentage of votes per candidate
# 5) The election winner (popular vote)

# import datetime as dt
# now = dt.datetime.now()
# print(f"The time right now is {now}")

import csv
import os
# Assign a variable for the file path to the file
# Use os.path.join("str","str") to make it work on either Mac or Windows OS
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a file (and file path) to save results to
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize the total vote counter
total_votes = 0

# Open the election results and read the file; use "with" so that it closes automatically
with open(file_to_load) as election_data:

    # Read the file with reader function
    file_reader = csv.reader(election_data)


    # Read and print the Header Row
    headers = next(file_reader)
    print(headers)

     # Print every row in the CSV file

    for row in file_reader:
        total_votes += 1
    
# Print total votes
print(total_votes)


'''
# Open file using "with" so that it automatically closes
with open(file_to_save) as outfile:
    
    # Code to read and analyze data here
    outfile.write("Counties in the Election\n-------------------------\n")
   outfile.write("Arapahoe\nDenver\nJefferson")
'''
