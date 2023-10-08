#import to txt file- code adapted from slack overflow https://stackoverflow.com/questions/74324797/how-to-export-python-printed-output-to-txt-file-at-the-end-of-code
import sys

sys.stdout= open('output.txt', 'w')

#restore standard output 
sys.stdout= sys.__stdout__

#Modules code adapted from class activites 3.2 acitivty 8
import os
import csv

# start total months counter by counting rows
total_rows= 0
    
#Set path for file
csvpath= os.path.join("..", "Resources", "budget_data.csv")

#open CSV using UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    
    #skip header row
    header= next(csvreader, None)

    #loop through data counting total months
    for row in csvreader:
        total_rows += 1
    
    #print the result of total months
    print(f"Total number of months in the dataset: {total_rows}") 
    
   
   
    #reset file to beginning
    csvfile.seek(0)
    
    #skip header row again
    header= next(csvreader, None)
    
    #loop through data for total sum of profits/ losses, start total at 0
    column_net_total= 0
    
    #Specifying column 2 to sum the total profits/ losses
    column_index_for_net_total= 1
    
    #loop through the rows and sum column 2 code adapted from slack overflow- https://stackoverflow.com/questions/65151369/summing-a-column-in-a-csv-file-using-python
    for row in csvreader:
        try:
            value=int(row[column_index_for_net_total])
            column_net_total += value
        except ValueError:
            pass
        
    #print result of total profits/ losses
    print(f"Net Total of Profits/ Losses{column_index_for_net_total}: ${column_net_total}")
    
   
   
    #reset file to beginning
    csvfile.seek(0)
    
    #skip header row again
    header= next(csvreader, None)
    
    #indicate initial variable starts at 0 and stores previous value for calcuating changes in profits/losses
    total_change=0 
    previous_value= None
    
    #loop through the rows and calculate changes in column 2 (profits/ losses)
    for row in csvreader:
        if len(row) > 1: #ensure row has 2 columns
            try: 
                current_value= int(row[1]) #convert column 2 to integer
                if previous_value is not None:
                    change= current_value-previous_value
                    total_change += change
                previous_value= current_value
            except ValueError:
                pass
            average_total_change= total_change/86
            
    #print total changes in profits
    print(f"Changes in profits/losses: ${average_total_change}")
    
    
    
    
     #reset file to beginning
    csvfile.seek(0)
    
    #skip header row again
    header= next(csvreader, None)
    
    #indicate initial variable starts at 0 for calculating greatest increase in profits
    greatest_increase= 0
    previous_value= None
    
    #loop throguh the rows and find the greatest increase in profit from column 2
    for row in csvreader:
        if len(row) > 1: # ensuring the row has 2 columns
            try: 
                current_value= int(row[1]) #converting to integer
                if previous_value is not None:
                    increase= current_value-previous_value
                    if increase > greatest_increase:
                        greatest_increase= increase
                previous_value=current_value
            except ValueError:
                pass
    
    #print greatest increase of profits
    print(f"Greatest increase in profits: ${greatest_increase}")
    
    
    
    #reset file to beginning
    csvfile.seek(0)
    
    #skip header row again
    header= next(csvreader, None)
    
    #indicate initial variable starts at 0 for calculating greatest decrease in profits
    greatest_decrease= 0 
    previous_value= None
    
    #loop through rows to find the greatest decrease in profit in column 2 
    for row in csvreader: 
        if len(row) > 1: #ensuring row has 2 columns
            try:
                current_value= int(row[1]) #converting to integer
                if previous_value is not None:
                    decrease= current_value- previous_value
                    if decrease < greatest_decrease:
                        greatest_decrease = decrease
                previous_value = current_value
            except ValueError:
                pass
    
    #print greatest decrease of profits
    print (f"Greatest decrease in profits: ${greatest_decrease}")
    

    
                

    
    
            
    
    
    
    
    
    
    

    
    
    