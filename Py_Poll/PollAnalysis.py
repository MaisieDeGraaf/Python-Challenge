import os
import csv

csv_path = r'Py_Poll\Resources\election_data.csv'

ballot_ID = []
Country = []
Candidate = []
Individual_Canditates = []
Candidate_Votes_1 = 0
Candidate_Votes_2 = 0
Candidate_Votes_3 = 0



with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        ballot_ID.append(row[0])
        Country.append(row[1])
        Candidate.append(row[2])

        Total_votes = len(ballot_ID)

    for i in Candidate:
        if i not in Individual_Canditates:
            Individual_Canditates.append(i)


    for i in Candidate:
        if i == Individual_Canditates[0]:
            Candidate_Votes_1 = Candidate_Votes_1 + 1
        if i == Individual_Canditates[1]:
            Candidate_Votes_2 = Candidate_Votes_2 + 1
        if i == Individual_Canditates[2]:
            Candidate_Votes_3 = Candidate_Votes_3 + 1

    Individual_Votes = [Candidate_Votes_1, Candidate_Votes_2, Candidate_Votes_3]
# The percentage of votes each candidate won
    
    winner_votes = max(Individual_Votes)
    # for winner in Individual_Votes:
    #     if winner > winner_votes:
    #         winner_votes = winner


print("Election Results")
print("_______________________________")
print(f"Total Votes: {Total_votes}")
print("_______________________________")
print(f"{Individual_Canditates[0]}: {round(Individual_Votes[0]/len(ballot_ID) * 100, 3)}% ({Individual_Votes[0]})")
print(f"{Individual_Canditates[1]}: {round(Individual_Votes[1]/len(ballot_ID) * 100, 3)}% ({Individual_Votes[1]})")
print(f"{Individual_Canditates[2]}: {round(Individual_Votes[2]/len(ballot_ID) * 100, 3)}% ({Individual_Votes[2]})")
print("_______________________________")
print(f"Winner: {Individual_Canditates[Individual_Votes.index(winner_votes)]}")
print("_______________________________")

Poll_Output_Path = r'C:\Users\qwert\Documents\GitHub\Python-Challenge\Py_Poll\Resources'
final_Output = os.path.join(Poll_Output_Path, "Poll_Output.txt")
with open(final_Output, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Election Results"])
    writer.writerow(["_______________________________"])
    writer.writerow([f"Total Votes: {Total_votes}"])
    writer.writerow(["_______________________________"])
    writer.writerow([f"{Individual_Canditates[0]}: {round(Individual_Votes[0]/len(ballot_ID) * 100, 3)}% ({Individual_Votes[0]})"])
    writer.writerow([f"{Individual_Canditates[1]}: {round(Individual_Votes[1]/len(ballot_ID) * 100, 3)}% ({Individual_Votes[1]})"])
    writer.writerow([f"{Individual_Canditates[2]}: {round(Individual_Votes[2]/len(ballot_ID) * 100, 3)}% ({Individual_Votes[2]})"])
    writer.writerow(["_______________________________"])
    writer.writerow([f"Winner: {Individual_Canditates[Individual_Votes.index(winner_votes)]}"])
    writer.writerow(["_______________________________"])