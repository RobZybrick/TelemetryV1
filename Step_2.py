# Using python, create CSV file with 5 rows and 5 columns with specified numbers
# Store the CSV file onto the desktop
# majority of the code referenced from -> https://www.geeksforgeeks.org/working-csv-files-python/
# file path location referenced from -> https://stackoverflow.com/questions/29715302/python-just-opening-a-csv-file-from-desktop-on-mac-os

# importing the csv module
import csv

# field names
fields = ['Number 1', 'Number 2', 'Number 3', 'Number 4', 'Number 5']

# data rows of csv file
rows = [ ['0', '1', '2', '3', '4'],
        ['5', '6', '7', '8', '9'],
        ['10', '11', '12', '13', '14'],
        ['50', '100', '150', '200', '250'],
        ['0', '10', '200', '3000', '4000'],
        ['-1', '-10', '-200', '-3000', '-4000']]

# name of csv file
#filename = "TelemetryV1_Milestron1_Method1.csv"

# writing to csv file
with open('/Users/rfzybrick/Desktop/TelemetryV1/Step2.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)
