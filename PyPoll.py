# The data we need to have and deliver to audit the election
# 1) Total # of votes in the election
# 2) List of candidates that received votes
# 3) Total # of votes per candidate
# 4) Percentage of votes per candidate
# 5) The election winner (popular vote)

#import datetime as dt
#now = dt.datetime.now()
#print(f"The time right now is {now}")

import csv
import os
# Assign a variable for the file path tot the file
# Use os.path.join("str","str") to make it work on either Mac or Windows
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a file to save results to
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as outfile:
    # Write some data
    outfile.write("Counties in the Election\n-------------------------\n")
    outfile.write("Arapahoe\nDenver\nJefferson")


# Open the election results and read the file
'''
with open(file_to_load) as election_data:

    # To do: perform analysis
    print(election_data)
'''
