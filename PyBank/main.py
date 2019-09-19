#Parse CSV into a data structure to operate on
#Calculate a summary with various fields
#Display summary and write to a text file

import os
import re
import csv

#Creates objects to input and out put
# Sample call:
# budget_data_csv, summary_out_txt = create_budget_io(budget_data.csv, Resources, analysis, summary.txt )
def create_budget_io(in_file, in_path, out_file, out_path):
    file_load = os.path.join(str(in_path), str(in_file))
    file_output = os.path.join(str(out_path), str(out_file))
    return file_load, file_output

#read_csv file to a list of tuples
def csv_to_list(csv_file):
   with open(csv_file) as file:
        budget_data = [tuple(line) for line in csv.reader(file)]
        return budget_data 

#read a csv to a dic with headers as key: value names

def csv_to_dic(csv_file):
    budget_data = {}
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        for dict_row in reader:
            date = dict_row["Date"]
            p_l = dict_row["Profit/Losses"]
            budget_data[date] = p_l
            #print(dict_row["Date"])            
    return  budget_data

#Testing and execution framework
budget_data_csv, summary_out_txt = create_budget_io('budget_data.csv', 'Resources', 'summary.txt', 'analysis')

budget_list = csv_to_list(budget_data_csv)
budget_dict = csv_to_dic(budget_data_csv)

max_p =budget_dict[f'{max (budget_dict, key=budget_dict.get)}']

#print(budget_list)
print(max_p)
