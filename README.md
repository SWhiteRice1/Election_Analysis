# Election_Analysis

## Project Overview
A Colorado Board of Election employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Get a total of votes cast to each county
4. Calculate the total number of votes cast form each county
5. Calulate the percentage of votes cast from each county
6. Determine which county had the largest voter turnout
7. Calculate the total number of votes each candidate received
8. Calculate the percentage of votes each candidate won
9. Determine the winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.38.1

## Summary
The analysis of the election show that:
- There were "369,711" votes cast in the election.
- The County results were:
  - Jefferson: 10.5%(38,855)
  - Denver: 82.8%(306,055)
  - Arapahoe: 6.7%(24,801)
- Denver had the largest county turnout.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
 - The candidate results were:
  - Charles Casper Stockham: received 23.05% of the vote.
  - Diana DeGette: received 73.81% of the vote.
  - Raymon Anthony Doane: received 3.14% of the vote.
 - The winner of the election was:
  - Diana DeGette, who received "73.8%" of the vote and "272,892" number of votes.
  
 ## Challenge Summary
 As the election commission reviews the results of this election and this script, the value of this script should be seen clearly. By utilizing this code, it will allow you to quickly analyze election results by county and candidate to determine the winner and where majority of the voters are from to determine the accuracy and reliability of the vote. To reuse the script, ensure the csv file path and txt files that are created are correct.
- The file path and txt.file can be corrected beginning in line 5 of the code as seen below:
```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("Resources", "election_analysis.txt")
```
Overall, this script is easilsy replicated and analyzed with simple updates to where to glean the data from for other congressional, senatorial, or even Presidental elections. However, presidential elections may also require to review by state which would require additional information on State in the election_results file.


