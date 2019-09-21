#Parse CSV into a data structure to operate on
#Calculate a summary with various fields
#Display summary and write to a text file

import os
import csv
import numpy as np
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
            p_l = float(dict_row["Profit/Losses"])
            budget_data[date] = p_l
            #print(dict_row["Date"])            
    return  budget_data

#given a value and a dictionary, this will spit out the first key that has value, remove the index[0] to get a list of all keys with matching value
def get_key(dictionary, value):
    target_key = str([key for key, target_value in dictionary.items() if target_value == value][0])
    return target_key

def min_max_kvp(dictionary):
    max_value = dictionary[f"{max (dictionary, key=dictionary.get)}"]
    min_value = dictionary[f"{min (dictionary, key=dictionary.get)}"]
    max_key = get_key(dictionary, max_value)
    min_key = get_key(dictionary, min_value)
    minimax_kvp = {"min": {min_key: int(min_value)}, 
                   "max": {max_key: int(max_value)}}
    return minimax_kvp

def avg_delta_pl(dictionary):
    delta = np.fromiter(dictionary.values(), dtype=int)
    delta = np.diff(delta)
    avg_delta = sum(delta)/len(delta)
    return avg_delta

#generates a financial like summary of some chosen statistics
def gen_summary(dictionary):
    month_count = len(dictionary)
    net_pl = sum(dictionary.values())
    avg_delta = avg_delta_pl(dictionary)
    minimax_kvp = min_max_kvp(dictionary)
    summary_financials = {"months": month_count,
                          "Net":   net_pl,
                          "Average Change": avg_delta,
                          "Greatest Loss": minimax_kvp["min"],
                          "Greatest Gain": minimax_kvp["max"]}
    return summary_financials

#this function will only work with the data we have. The summary dictionary and the text output is dictated by the needs of the stakeholders.
def print_summary(dictionary):
    summary = gen_summary(dictionary)
    summary_text = f'Financial Analysis\n----------------------------\nMonths: {summary["months"]}\nTotal: {summary["Net"]}\nGreatest Decrease: {summary["Greatest Loss"]}\nGreatest Increase: {summary["Greatest Gain"]}'
    print(summary_text)
    return summary_text

def summary_to_file(summary,file_output):
    with open(file_output, "w", newline="") as data_file:
        data_file.write(summary)


#Testing and execution framework
budget_data_csv, summary_out_txt = create_budget_io("budget_data.csv", "Resources", "summary.txt", "analysis")
budget_dict = csv_to_dic(budget_data_csv)
# summary = gen_summary(budget_dict)
# print(f'Financial Analysis\n----------------------------\nMonths: {summary["months"]}\nTotal: {summary["Net"]}\nGreatest Decrease: {summary["Greatest Loss"]}\nGreatest Increase: {summary["Greatest Gain"]}')

summary = print_summary(budget_dict)
summary_to_file(summary,summary_out_txt)


# month_count = len(budget_dict)    
# summary = min_max_kvp(budget_dict)
# total = sum(budget_dict.values())
# change = avg_delta_pl(budget_dict)

# print(budget_dict.values())
# print(month_count)
# print(summary)
# print(total)
# print(change)
# max_p = budget_dict[f"{max (budget_dict, key=budget_dict.get)}"]
# max_date =str([key for key, value in budget_dict.items() if value == max_p][0])

#print(budget_list)
# print(max_p)
# print(max_date)


