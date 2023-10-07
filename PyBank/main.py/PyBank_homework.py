#Modules
import os
import csv

# start total months counter
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
    
    #print the result
    print(f"Total number of months in the dataset: {total_rows}") 