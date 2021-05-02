# Import CSV file
import os
import csv

# Specify the path for the csv file
csvpath = os.path.join(r"D:\036_Rice\1_Homework_UD\Python_Challenge\PyBank\Resources\budget_data.csv")

#Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader (csvfile,delimiter=",")

# Loop
    for row in csvreader:
        print(row)
print (type(row[1]))

