#import files
import os
import csv

# Path to collect data from the Resources folder
poll_analysis = os.path.join('..','resources','election_data.csv')

# Create empty lists to iterate through specific rows for the following variables
votes=0
khan_votes=0
correy_votes=0
li_votes=0
otooley_votes=0

# Open and read csv
with open(poll_analysis) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (beacause there is a header)
    header= next(csv_reader)

    for row in csv_reader: 
        votes=votes+1 #The total number of votes cast
        
    # Calculate Total of votes for each candidate(I reckon tht there is a  easy way to do this with loops, like in the bank analysis, it just I do not how to # list of candidates who received votes, I just fliter in excel; 4 candidates)
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1

    # #The percentage of votes each candidate won

    khan_percent = khan_votes / votes
    correy_percent = correy_votes / votes
    li_percent = li_votes / votes
    otooley_percent = otooley_votes / votes

    #The winner of the election based on popular vote
    winner=max(khan_votes,correy_votes,li_votes,otooley_votes)  

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# Print values_staments
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {votes}")
print(f"---------------------------")
print(f"Khan: {khan_percent}% ({khan_votes})")
print(f"Correy: {correy_percent}% ({correy_votes})")
print(f"Li: {li_percent}% ({li_votes})")
print(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

#output file   
output_file = os.path.join("..","Analysis","Election Summary.txt" )

with open(output_file,"w") as txtfile:

   txtfile.write(f"Election Results")
   txtfile.write("\n")
   txtfile.write(f"---------------------------")
   txtfile.write("\n")
   txtfile.write(f"Total Votes: {votes}")
   txtfile.write("\n")
   txtfile.write(f"---------------------------")
   txtfile.write("\n")
   txtfile.write(f"Khan: {khan_percent} ({khan_votes})")
   txtfile.write("\n")
   txtfile.write(f"Correy: {correy_percent} ({correy_votes})")
   txtfile.write("\n")
   txtfile.write(f"Li: {li_percent} ({li_votes})")
   txtfile.write("\n")
   txtfile.write(f"O'Tooley: {otooley_percent} ({otooley_votes})")
   txtfile.write("\n")
   txtfile.write(f"---------------------------")
   txtfile.write("\n")
   txtfile.write(f"Winner: {winner_name}")
   txtfile.write("\n")
   txtfile.write(f"---------------------------")