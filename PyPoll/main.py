import os as OS
import csv as CSV

file_path_read = OS.path.join('Resources','election_data.csv')
file_path_write = OS.path.join('analysis','Election_Results.txt')

output_dict = {}

col_candidate = 2

voters = 0

with open(file_path_read,'r') as csv_file:
    csv_reader = CSV.reader(csv_file, delimiter=',')
    next(csv_reader)
    for csv_line in csv_reader:
        voters += 1
        if csv_line[col_candidate] not in output_dict.keys():
            output_dict[csv_line[col_candidate]] = 1
        else:
            output_dict[csv_line[col_candidate]] += 1


with open(file_path_write,'w',newline='') as txt_file:
    txt_write = CSV.writer(txt_file)

    text_temp = '\nElection Results\n'
    text_temp += '-------------------------\n'
    text_temp += f'Total Votes : {voters}\n'
    text_temp += '-------------------------\n'

    for i in output_dict:
        text_temp += f'{i} : {(output_dict[i]/voters*100):.3f}% ({output_dict[i]})\n'
    
    text_temp += '-------------------------\n'
    text_temp += f'Winner : {max(output_dict,key=output_dict.get)}\n'
    text_temp += '-------------------------\n'
    
    txt_write.writerow([text_temp])
    print(text_temp)