#Data Needed:
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote
##Path of resource: Resources/election_results.csv
import csv
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)
# Finding indirect path
##use os.path.join("Folder","File_name")
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)
<open file 'Resources/election_results.csv', mode 'r' at 0x10479c780>