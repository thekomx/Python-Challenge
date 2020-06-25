import os as OS
import csv as CSV

file_path_read = OS.path.join('Resources','election_data.csv')      #Input File
file_path_write = OS.path.join('analysis','Election_Results.txt')   #Output File

output_dict = {}    #Dictionary for output

col_candidate = 2   #Input data row index

voters = 0          #Initialize number of vote

with open(file_path_read,'r') as csv_file:
    csv_reader = CSV.reader(csv_file, delimiter=',')

    next(csv_reader)    #Skip first row as it is header

    for csv_line in csv_reader:
        voters += 1     #Counting number of vote

        # -- Check if the candidate exists in the output dictionary key
        # -- If not means this is candidate first vote, then add candidate to the kay and add 1 vote to value
        if csv_line[col_candidate] not in output_dict.keys():
            output_dict[csv_line[col_candidate]] = 1
        else:
            output_dict[csv_line[col_candidate]] += 1


#Output to text file and display 
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