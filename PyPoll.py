import os 
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
election_data_csv_path= os.path.join('/Users/michaelpeyser/Desktop/Challenge/python-challenge/PyPoll/Resources/election_data.csv')


with open(election_data_csv_path, 'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    csv_header= next(csvreader)

    total_votes= 0
    candidates=[]
    candidate_votes=[]
    winner=""

    for row in csvreader:
        total_votes +=1
        candidate_location= (row[2])
        if candidate_location in candidates:
            candidate_index= candidates.index(candidate_location)
            candidate_votes[candidate_index]= candidate_votes[candidate_index] + 1
        else:
            candidates.append(candidate_location)
            candidate_votes.append(1)

        percentage=[]
        max_votes=0
        max_index=0
        

    for y in range(len(candidates)):
        percent_vote= round(candidate_votes[y]/total_votes*100, 2)
        percentage.append(percent_vote)
        if candidate_votes[y]> max_votes:
            max_votes=candidate_votes[y]
            max_index=y
            winner=candidates[max_index]
        #print(winner)
        

print("-----------------------------------")
print("        Election Results           ")
print("-----------------------------------")
print(f'Total Votes: {total_votes}')
print("-----------------------------------")
for y in range(len(candidates)):
    print(f'{candidates[y]} : {percentage[y]}% ({candidate_votes[y]})')
print("-----------------------------------")
print('Election Winner: ' + str(winner))
print("-----------------------------------")