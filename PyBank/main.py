#Parse CSV into a data structure to operate on
#Calculate a summary with various fields
#Display summary and write to a text file

import os
import re
import csv

#Creates objects to input and out put
# Sample call:
# budge_data_csv, summary_out_txt = create_budget_io(budget_data.csv, Resources, analysis, summary.txt )
def create_budget_io(in_file, in_path, out_file, out_path):
    file_load = os.path.join(str(in_path), str(in_file))
    file_output = os.path.join(str(out_path), str(out_file))
    return file_load, file_output

# The date has format MMM-YYY Delimiter is ','
# Takes a string from our data set 
# This is annoying because we have negative values in one column
# While also using a dash in the date. Introduce a two step split:
# Sample call:
# reader
def split_to_tuple(csv_row, delim_1, delim_2):
    date, p_l = csv_row.split(f'{delim_1}')
    month, year = date.split(f'{delim_2}')
    year, month, p_l =split_row
    return split_row


    