
#import files 
import os
import csv

#Export files
file_to_output = "Resources/budget_analysis.txt"

#definition of variables
Total_months=0
Net_total=0
Average_total=0
greates_increase=0
greates_increase_date=0
greatest_decrease=0
greatest_decrease_date=0

# Set Path For File
csvpath = os.path.join('.', 'PyBank', 'Resources', '02-PyBank_Resources_budget_data.csv')

# Open & Read CSV File
with open(csvpath, newline='') as csvfile:

# CSV Reader Specifies Delimiter & Variable That Holds Contents
     csvreader = csv.reader(csvfile,delimiter=",")

     print(csvreader)
    
# Read the header row first (skip this part if there is no header)
csv_header = next(csv_file)

#Read through each row of data after the header
for row in csvreader:

# Calculate the totals
Total_months= Total_months + 1
total_revenue = total_revenue +len(row["Profit/Losses"])
revenue_change = int(row["Revenue"]) - prev_revenue
