
#import files 
import os
import csv

# Path to collect data from the Resources folder
budget_analysis = os.path.join('..','resources','budget_data.csv')

# Create empty lists to iterate through specific rows for the following variables
months =[]
total_profit = []
monthly_profit_change = []

# Open and read csv
with open(budget_analysis) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (beacause there is a header)
    header= next(csv_reader)
    for row in csv_reader: 
        months.append(row[0]) # Append the total months and total profit to their corresponding lists(the loop will go every time to the row and ad the next row)
        total_profit.append(int(row[1]))  # We want value into an integer number for the profits
    
    # The average of the changes in "Profit/Losses" over the entire period
    
    x=0
    for x in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[x+1]-total_profit[x])  

        # Obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)


    #The greatest increase in profits (date and amount) over the entire period
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
    #The greatest decrease in losses (date and amount) over the entire period
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print values_staments

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease_value))})")

#output file
output_file = os.path.join("..","Analysis","Financial Summary.txt" )

with open(output_file,"w") as txtfile:

   txtfile.write(f"Financial Summary")
   txtfile.write(f"---------------------------")
   txtfile.write(f"Total Months:" +str(len(months)))
   txtfile.write(f"Total: $"+str(total_profit))
   txtfile.write(f"Average Change: $"+str(monthly_profit_change))
   txtfile.write(f"Greatest Increase in Profits: {max_increase_month} ${max_increase_value}")
   txtfile.write(f"Greatest Decrease in Profits: {max_decrease_month} ${max_decrease_value}")

