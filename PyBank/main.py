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
inc_index = Delta.index(increase)
inc_mon = Months[inc_index]

decrease = min (Delta)
dec_index = Delta.index(decrease)
dec_mon = Months[dec_index]

# print results
print ("Financial Analysis")
print ("------------------")
print (f"Total Months: {Count_Months} months")
print (f"Total Amount: $ {Total_Amount:,}")
print (f"Average Change: $ {Average:,} ")
print (f"Greatest Increase in Profits: $ {increase:,} in {inc_mon}")
print (f"Greatest Decrease in Profits: $ {decrease:,} in {dec_mon}")

# prints for verification
# print(row)
# print (type(row[1]))
# print (Months)
# print (Delta)
# print (increase)
# print (decrease)
# print (inc_mon)
# print (dec_mon)

# export to a txt file
txt_file = os.path.join (r"D:\036_Rice\1_Homework_UD\Python_Challenge\PyBank\Output\Financial_Analysis.txt")
with open (txt_file,"w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("------------------\n")
    outfile.write(f"Total Months: {Count_Months} months\n")
    outfile.write(f"Total Amount: $ {Total_Amount:,}\n")
    outfile.write(f"Average Change: $ {Average:,}\n")
    outfile.write(f"Greatest Increase in Profits: $ {increase:,} in {inc_mon}\n")
    outfile.write(f"Greatest Decrease in Profits: $ {decrease:,} in {dec_mon}\n")