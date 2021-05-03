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
    Amounts=[]
    Total_Amount = 0


    # Loop
    for row in csvreader:
        Months = Months + 1
        Amounts.append (int(row[1]))
        Total_Amount = sum(Amounts)
    
#print(row)
#print (type(row[1]))

print ("Financial Analysis")
print ("------------------")
print (f"Total Months: {Months} months")
print (f"Total Amount: {Total_Amount}")
print (f"Average Change: ")
print ("Greatest Increase in Profits: ")
print ("Greatest Decrease in Profits: ")
