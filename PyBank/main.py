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
    Count_Months = 0
    Amounts=[]
    Total_Amount = 0
    Prev_Amount = 0
    Curr_Amount = 0
    Delta = []
    Months = []
        
    # Loop
    for row in csvreader:
        Count_Months = Count_Months + 1
        Amounts.append (int(row[1]))
        Total_Amount = sum(Amounts)
        Curr_Amount = int(row[1])

    # Conditional for Change Average
        if Count_Months == 1:
            Prev_Amount = Curr_Amount
            continue
        else:
            # calculate the change amount in a given month
            delta = Curr_Amount - Prev_Amount
            # generate the list of the months
            Months.append(row[0])
            # generate the list with the deltas
            Delta.append(delta)
            # stop the loop
            Prev_Amount = Curr_Amount
# calculate average change 
Total = sum (Delta)
Average = round(Total/(Count_Months-1),)
# calculate greatest increase and decrease
increase = max (Delta)
decrease = min (Delta)



#print(row)
#print (type(row[1]))

print ("Financial Analysis")
print ("------------------")
print (f"Total Months: {Count_Months} months")
print (f"Total Amount: {Total_Amount:,}")
print (f"Average Change: {Average:,} ")
print ("Greatest Increase in Profits: ")
print ("Greatest Decrease in Profits: ")
# print (Months)
# print (Delta)
print (increase)
print (decrease)