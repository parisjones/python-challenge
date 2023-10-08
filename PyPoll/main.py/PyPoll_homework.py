#import to txt file- code adapted from slack overflow https://stackoverflow.com/questions/74324797/how-to-export-python-printed-output-to-txt-file-at-the-end-of-code
import sys

sys.stdout= open('output.txt', 'w')

#restore standard output 
sys.stdout= sys.__stdout__


#Modules code adapted from class activites 3.2 acitivty 8
import os
import csv

#start total vote counter at 0 by counting rows
total_rows= 0

#Set path for file
csvpath= os.path.join("..", "Resources", "election_data.csv")

#open CSV using UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    
    #skip header row
    header= next(csvreader, None)

    #loop through data counting total votes
    for row in csvreader:
        total_rows += 1
    
    #print the result of total votes
    print(f"Total number of votes in the dataset: {total_rows}") 
    
    
    
    #reset file to beginning to loop through column 3 to ID names of candidates, number of votes, and percentage of votes
    csvfile.seek(0)
    
    #skip header row again
    header= next(csvreader, None)
    
    #start a dictionary to store the name count
    name_counts= {}
    
    #loop through the rows and count the names in column 3 -code adapted from slack overflow- https://stackoverflow.com/questions/65151369/summing-a-column-in-a-csv-file-using-python
    for row in csvreader:
        if len(row) > 2: #check if row has at least  3 columns
            name= row[2] #since the names are in the 3rd column
            
            #update name count in dictionary
            if name in name_counts:
                name_counts[name] += 1
            else: 
                name_counts[name]=1
                
    #print results including name and frequency voted for
    for name, count in name_counts.items():
        print(f"{name}: {count}")
        
#calculate percentage for each name
percentage_results= {}
for name, count in name_counts.items(): 
    percentage= (count/ total_rows) * 100
    percentage_results[name]= percentage
    
#print results
for name, percentage in percentage_results.items():
    print(f"{name}: {percentage: .2f}%")
    
#define winner by finding the name repeated the most
most_voted_candidate= max(name_counts, key=name_counts.get)
        
#print results
print(f"Winner: {most_voted_candidate}")     




