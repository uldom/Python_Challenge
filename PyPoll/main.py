# Import CSV
import os
import csv

# Specify the path for the csv file
csvpath = os.path.join(r"D:\036_Rice\1_Homework_UD\Python_Challenge\PyPoll\Resources\election_data.csv")

# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader,None)
    #print (csv_header)

    # Declare variables
    count_votes = 0
    votes = []
    total_votes = 0
    count_names = 0
    names = []
    set_names = []
    percent_votes = 0
    percent = []

    # Loop
    for row in csvreader:
        total_votes = total_votes + 1
        
        # generate the list with the candidates
        names.append(row[2])
        

print(total_votes)        
