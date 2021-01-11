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

# initialize the total vote counter, candidate list, candidates votes dictionary
total_votes = 0
candidate_options = []
candidate_votes = {}

# initialize the winning candidate, the winning vote count, and the winning percentage
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# Open the election results and read the file; use "with" so that it closes automatically
with open(file_to_load) as election_data:

    # Read the file with reader function
    file_reader = csv.reader(election_data)

    # Read and print the Header Row
    headers = next(file_reader)
    # print(headers)

    # Tally the total number of votes
    for row in file_reader:
        total_votes += 1

        # Print the candidate name from each row and add to options list if it isn't in the list already
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Initialize that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Begin counting that candidates votes
        candidate_votes[candidate_name] += 1

'''
for cand in candidate_votes:
    votes = candidate_votes[cand]
    vote_percentage = float(votes)/total_votes * 100

    # print(f'Candidate {cand} received {vote_percentage:.1f} % of the vote.')

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = cand

    # print(f"{cand}: {vote_percentage:.1f}% ({votes:,})\n")

# Print winning candidate
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n"
    f"-------------------------\n")

# print(winning_candidate_summary)

# Print total votes, candidate options
# print(total_votes)
# print(candidate_options)
# print(candidate_votes)
'''
# Open file using "with" so that it automatically closes
with open(file_to_save, 'w') as txt_file:

   # Organize election results starting with a totl votes overview
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    # Print to terminal
    print(election_results, end="")
    # Write to text file
    txt_file.write(election_results)

    # Iterate through the candidates and calculate their total votes and vote percentage
    for cand in candidate_votes:
        votes = candidate_votes[cand]
        vote_percentage = float(votes)/total_votes * 100
        # Format results
        candidate_results = (f'{cand}: {vote_percentage:.1f}% {votes:,}\n')
        # Print to terminal
        print(candidate_results)
        # Write to text file
        txt_file.write(candidate_results)

        # Determine the winning candidate and there vote count and percentage
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = cand

    # Format a summary highlighting the winning candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    # Print to terminal
    print(winning_candidate_summary)
    # Write to text file
    txt_file.write(winning_candidate_summary)


# CHALLENGE
# 1) Voter Turnout for each county
# 2) The percentage of votes from each county out of the total count
# 3) The county with the higherst turnout
