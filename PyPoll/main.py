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

#Counters are special dictionary objects that have methods for quick
#tallies
#Testing and Executionqq


election_csv, results_out_txt = create_election_io("election_data.csv", "Resources", "election_results.txt", "analysis")
election_tally = csv_to_list(election_csv)
tally = Counter()
vote_percentage = []
for candidate in election_tally[1:]:
    tally[candidate] += 1
vote_total = sum(tally.values())
winner = get_key(tally, max(tally.values()))
for vote_count in tally.values():
    vote_percentage.append((vote_count/vote_total, vote_count))




# election_set = set(election_tally[1:])
print(election_tally[1:10])
# print(election_set)
print(tally)
print(sum(tally.values()))
print(vote_percentage)

print (winner)
