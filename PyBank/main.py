# HOMEWORK MODULE 03 - PYBANK

# Importing the "os" module - to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Store the CSV file path in a variable called filepath
filepath = os.path.join('Resources','budget_data.csv')

# Creating lists to add the csv values to
monthslist = []
pro_los = []
changes = []
    
# Reading using CSV module
with open(filepath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row, so the code will skip the header row
    header = next(csvreader)

    # Going through each row of data and adding them to the lists
    for row in csvreader:
        #Recording the dates in a list  
        monthslist.append(row[0])
        #Recording the Profits and Losses
        pro_los.append(int(row[1]))

    # Analysing the profits/losses changings    
    for i in range(len(pro_los)-1):
        changes.append(pro_los[i+1]-pro_los[i]) 

    # Evaluating the max and min from the list made
    increase = max(changes)
    decrease = min(changes)

    # Correlating Greatest Increase and the Greatest Decrease with respective months though indexes
    grincrease = changes.index(max(changes))+1
    grdecrease = changes.index(min(changes))+1

# Printing results in the terminal

print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months:{len(monthslist)}")
print(f"Total: ${sum(pro_los)}")
print(f"Average Change: {round(sum(changes)/len(changes),2)}")
print(f"Greatest Increase in Profits: {monthslist[grincrease]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {monthslist[grdecrease]} (${(str(decrease))})")  

#EXPORTING THE RESULTS TO A TEXT FILE

resultspath = os.path.join('analysis','results_pybank.txt')
text =   (
    "Financial Analysis\n"
    "------------------------\n"
    f"Total Months:{len(monthslist)}\n"
    f"Total: ${sum(pro_los)}\n"
    f"Average Change: {round(sum(changes)/len(changes),2)}\n"
    f"Greatest Increase in Profits: {monthslist[grincrease]} (${(str(increase))})\n"
    f"Greatest Decrease in Profits: {monthslist[grdecrease]} (${(str(decrease))})\n")

with open(resultspath,"w") as results:
    results.write(text)

    
