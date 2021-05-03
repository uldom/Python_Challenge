# Import CSV file
import os
import csv

# Specify the path for the csv file
csvpath = os.path.join(r"D:\036_Rice\1_Homework_UD\Python_Challenge\PyBank\Resources\budget_data.csv")

# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader (csvfile,delimiter=",")
    print(csvreader)
    csv_header = next(csvreader,None)
    # Declare variables
    Months = 0
    Total_amount=[]
    
    # Loop
    for row in csvreader:
        months = months + 1
        Total_amount.append (int(row[1]))
    
    
#print(row)
#print (type(row[1]))

print ("Financial Analysis")
print ("------------------")
print (f"Total Months: {Months} months")
print ("Total Amount:")
print ("Average Change:")
print ("Greatest Increase in Profits:")
print ("Greatest Decrease in Profits:")