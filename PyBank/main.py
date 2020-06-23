import os as OS
import csv as CSV

file_path_read = OS.path.join('Resources','budget_data.csv')
file_path_write = OS.path.join('analysis','Financial_Analysis.txt')

output_total_month = 'Total Months'
output_total = 'Total'
output_avg_change = 'Average  Change'
output_GIP = 'Greatest Increase in Profits'
output_GDP = 'Greatest Decrease in Profits'
output_dict = {output_total_month:0,output_total:0,output_avg_change:0,output_GIP:'',output_GDP:''}

col_month = 0
col_value = 1

with open(file_path_read,'r') as csv_file:
    csv_reader = CSV.reader(csv_file,delimiter=',')
    next(csv_reader)
    for csv_line in csv_reader:
        output_dict[output_total_month] += 1
        int_value = int(csv_line[col_value])
        output_dict[output_total] += int_value
        if output_dict[output_GIP] == '':
            greatest_increase = int_value
            greatest_decrease = int_value
            output_dict[output_GIP] = f'{csv_line[col_month]} (${int_value})'
            output_dict[output_GDP] = f'{csv_line[col_month]} (${int_value})'
        else:
            if int_value > greatest_increase :
                greatest_increase = int_value
                output_dict[output_GIP] = f'{csv_line[col_month]} (${int_value})'
            elif int_value < greatest_decrease :
                greatest_decrease = int_value
                output_dict[output_GDP] = f'{csv_line[col_month]} (${int_value})'
    
    output_dict[output_avg_change] = int(output_dict[output_total] / output_dict[output_total_month])
    
    
    
with open(file_path_write,'w',newline='') as txt_file :
    txt_writer = CSV.writer(txt_file)
    text_tmp = 'Financial Analysis'
    txt_writer.writerow([text_tmp])
    print(text_tmp)
    text_tmp = '---------------------------------------'
    txt_writer.writerow([text_tmp])
    print(text_tmp)
    for i in output_dict:
        text_tmp = f'{i} : {output_dict[i]}'
        txt_writer.writerow([text_tmp])
        print(text_tmp)
