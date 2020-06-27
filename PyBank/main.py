import os as OS
import csv as CSV

file_path_read = OS.path.join('Resources','Budget_Data.csv')            #Input file
file_path_write = OS.path.join('Analysis','Financial_Analysis.txt')     #Output file

# ----- Put output data in Dictionary ------------------------------------------------
# ----- The item key's name is the output title 
output_total_month = 'Total Months'
output_total = 'Total'
output_avg_change = 'Average  Change'
output_GIP = 'Greatest Increase in Profits'
output_GDP = 'Greatest Decrease in Profits'
output_dict = {output_total_month:0,output_total:0,output_avg_change:0,output_GIP:'',output_GDP:''}
#--------------------------------------------------------------------------------------

#Input data column index
col_month = 0
col_value = 1

with open(file_path_read,'r') as csv_file:
    csv_reader = CSV.reader(csv_file,delimiter=',')

    next(csv_reader)    #Skip first row as it is header

    for csv_line in csv_reader:
        output_dict[output_total_month] += 1    #Counting number of months
        int_value = int(csv_line[col_value])    #Store Integer converted value for multiple times uses
        output_dict[output_total] += int_value  #Counting Profit/Loss values

        # -- If this "TRUE" means this is the first row of data,
        # -- Then initialize output dictionary by give them the first row values
        if output_dict[output_GIP] == '':
            first_value = int_value         #For "average of change" formula uses
            greatest_increase = int_value       
            greatest_decrease = int_value
            output_dict[output_GIP] = f'{csv_line[col_month]} (${int_value})'
            output_dict[output_GDP] = f'{csv_line[col_month]} (${int_value})'
        else: 
            output_dict[output_avg_change] = int_value  #This will store the latest month value for "average of change" formula uses
            
            # -- If it not the first row 
            # -- change the MAX and MIN values if found new MAX and MIN
            if int_value > greatest_increase :
                greatest_increase = int_value
                output_dict[output_GIP] = f'{csv_line[col_month]} (${int_value})'
            elif int_value < greatest_decrease :
                greatest_decrease = int_value
                output_dict[output_GDP] = f'{csv_line[col_month]} (${int_value})'
            
    
    #Calculate "average of change"
    #The formula (First_Value - Last_Value)/(Time_Start - Time_End)
    output_dict[output_avg_change] = f'{((output_dict[output_avg_change] - first_value) / (output_dict[output_total_month] - 1)):.2f}'
    
    
#Output to text file and display    
with open(file_path_write,'w',newline='') as txt_file :
    txt_writer = CSV.writer(txt_file)
    text_tmp = '\nFinancial Analysis\n'
    text_tmp += '---------------------------------------\n'

    for i in output_dict:
        text_tmp += f'{i} : {output_dict[i]}\n'

    txt_writer.writerow([text_tmp])
    print(text_tmp)
