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
election_data.close()
file_to_save="Resources/election_results.csv"
open(file_to_save, "w")
election_data.close()
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
# Write three counties to the file.
     # Write three counties to the file.
     txt_file.write("Arapahoe")
     txt_file.write("Denver")
     txt_file.write("Jefferson")
with open(file_to_save, "w") as txt_file:
     txt_file.write("Arapahoe")
     txt_file.write("Denver")
     txt_file.write("Jefferson")
          # Write three counties to the file.
     txt_file.write("Arapahoe, Denver, Jefferson")
with open(file_to_save, "w") as txt_file:
     txt_file.write("Arapahoe, Denver, Jefferson")
with open(file_to_save, "w") as txt_file:
     txt_file.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson")
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
     
    # To do: read and analyze the data here.
       # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     for row in file_reader:
          print(row)
    #Print each row in the CSV file.
       # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     headers = next(file_reader)
     print(headers)  
    # Print the header row.
 # Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes=0
# Candidate option
candidate_options=[]
#Declare an empty dictionary
candidate_votes={}
#Declare a variable that holds and empty string value for the winning candidate
winning_candidate=""
#Declare a variable for the "winning_count" equal to zero
winning_count=0
#Declare a variable for the "winning_percentage" equal to zero
winning_percentage=0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
   
# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0

          #Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1
        
    with open(file_to_save, "w") as txt_file:
          # Print the final vote count to the terminal.
     election_results = (
          f"\nElection Results\n"
          f"-------------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"-------------------------\n")
     print(election_results, end="")
     # Save the final vote count to the text file.
     txt_file.write(election_results)
     # Determine the percentage of votes for each candidate by looping through the counts.
     # 1. Iterate through the candidate list.
     for candidate_name in candidate_votes:
     # 2. Retrieve vote count of a candidate.
               votes = candidate_votes[candidate_name]
     # 3. Calculate the percentage of votes.
               vote_percentage = float(votes) / float(total_votes) * 100
     # 4. Print the candidate name and percentage of votes.
               #print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")
               #  To do: print out each candidate's name, vote count, and percentage of
     # votes to the terminal.
     # To do: print out each candidate's name, vote count, and percentage of
     # votes to the terminal.
               candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
               #Determine if the vote count that was calculated is greater than the winning count
               # Print each candidate, their voter count, and percentage to the terminal.
               print(candidate_results)
               #  Save the candidate results to our text file.
               txt_file.write(candidate_results)
               if (votes > winning_count) and (vote_percentage>winning_percentage):
                    #2. If true then set winning_count = votes and winning-percent =
                    #vote_percentage
                    winning_count=votes
                    winning_percentage=vote_percentage
                    # Set winning_candidate equal to the candidates's name
                    winning_candidate=candidate_name
          
     winning_candidate_summary = (
               f"-------------------------\n"
               f"Winner: {winning_candidate}\n"
               f"Winning Vote Count: {winning_count:,}\n"
               f"Winning Percentage: {winning_percentage:.1f}%\n"
               f"-------------------------\n")
     print(winning_candidate_summary)
     # Save the winning candidate's name to the text file.
     txt_file.write(winning_candidate_summary)
     # Print the candidate list.
     #print(candidate_options)
     #Print the candidate vote dictionary
     #print(candidate_votes)

