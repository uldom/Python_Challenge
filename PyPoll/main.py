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

    # Loop for counting total of votes
    for row in csvreader:
        total_votes = total_votes + 1
        # generate the list with the set of candidates
        names.append(row[2])
    # Loop for identifying unique candidates
    for c in set (names):
        set_names.append(c)
        count_votes = names.count(c)
        votes.append(count_votes)    
        percent_votes = (count_votes/total_votes)*100
        percent.append(percent_votes)

max_votes = max(votes)
winner = set_names[votes.index(max_votes)]

# print results
print("Election Results")
print("-------------------------------")
print(f"Total {total_votes:,} votes")        
print("-------------------------------")

# Print the results in one row
for r in range(len(set_names)):
    print(f"{set_names[r]}: {votes[r]:,} votes, {round(percent[r],0)} %")
# print(set_names)
# print(votes)
# print(percent)
print("-------------------------------")
print(f"The winner of this election is: Mr. {winner}!")

# export to a txt file
txt_file = os.path.join (r"D:\036_Rice\1_Homework_UD\Python_Challenge\PyPoll\Output\Election_Results.txt")
with open (txt_file,"w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------------\n")
    outfile.write(f"Total {total_votes:,} votes\n")
    outfile.write("-------------------------------\n")
    for r in range(len(set_names)):
        outfile.write(f"{set_names[r]}: {votes[r]:,} votes, {round(percent[r],0)} %\n")
    outfile.write("-------------------------------\n")     
    outfile.write(f"The winner of this election is: Mr. {winner}!")