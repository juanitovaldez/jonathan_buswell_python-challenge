import os
import csv
from collections import Counter

#Function definitions to call and create our dictionary objects
def create_election_io(in_file, in_path, out_file, out_path):
    file_load = os.path.join(str(in_path), str(in_file))
    file_output = os.path.join(str(out_path), str(out_file))
    return file_load, file_output
# We are only interested in the count of unique candidates
# A list is just simple enough to deal with
def csv_to_list(csv_file):
   with open(csv_file) as file:
        election_data = [line[2] for line in csv.reader(file)]
        return election_data 

def get_key(dictionary, value):
    target_key = str([key for key, target_value in dictionary.items() if target_value == value][0])
    return target_key

#nasty catchall for previously prototyped code
def tabulate(dictionary):
    tally = Counter()
    vote_percentage = []
    for candidate in election_tally[1:]:
        tally[candidate] += 1
    vote_total = sum(tally.values())
    winner = get_key(tally, max(tally.values()))
    for vote_count in tally.values():
        vote_percentage.append(round(vote_count/vote_total, 4))
    candidates = dict(tally)
    text_candi = str()
    i = 0
    for entry in candidates:
        text_candi += f'{entry}:    ({vote_percentage[i]}) {candidates[entry]}   \n'
        i += 1
    tab_summary = {"Total Votes": int(vote_total),
                   "Candidates": text_candi,
                   "Winner": str(winner)}
    return tab_summary
def print_summary(dictionary):
    summary = tabulate(dictionary)
    summary_text = f'Election Results\n----------------------------\nTotal Votes: {summary["Total Votes"]}\n----------------------------\n{summary["Candidates"]}\nWinner: {summary["Winner"]}\n'
    print(summary_text)
    return summary_text

def summary_to_file(summary,file_output):
    with open(file_output, "w", newline="") as data_file:
        data_file.write(summary)

#Runs the our functions
election_csv, results_out_txt = create_election_io("election_data.csv", "Resources", "election_results.txt", "analysis")
election_tally = csv_to_list(election_csv)
summary = print_summary(election_tally)
summary_to_file(summary, results_out_txt)

