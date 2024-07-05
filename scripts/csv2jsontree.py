import csv
import json

# Define file paths: input, output
csv_file_path = '../files/file.csv'
json_file_path = '../files/file.json'

'''
This script if for an specific shape of csv file to be converted to json of a specific shape.

Expected shape of the csv input file:

Region,A,B,C,D
North,1,2,3,4
South,5,6,7,8

To be converted to json, specified shape, as:
[
    "A": {
        "North": 1,
        "South": 5,
        "East": 9,
        "West": 13
    },
    "B": {
        "North": 2,
        "South": 6,
        "East": 10,
        "West": 14
    }, ...
]

"Region" item will not be included in the json output.
'''

# Output a json file with the specified shape format.
# Each activity will be an object with regions as keys
# Each region will have a value for the activity

# function
def csv_to_json(csv_file, json_file):
    # Initialize a dictionary to store the activities from the csv file.
    # Expected to receive: [['Region','A','B','C','D'],['North',1,2,3,4],['South',5,6,7,8]]
    # Expected to store:   [ "A": { "North": 1, "South": 5, "East": 9, "West": 13 }, "B": { "North": 2, "South": 6, "East": 10, "West": 14 }, ]
    # Initialize as empty list.
    # This dictionary will store each activity as a key, with another dictionary as its value, mapping regions to their respective values for that activity.
    activities = {}

    # Bugfix: Before removing the 'Region' column, store all region values
    # to fix the bug at 
    # activities[activity][row['Region']] = float(row[activity])
    # then use the temp storage when setting the values in the activities dictionary
    regions = [] 

    # Read the input CSV file, open.
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        '''
        Expected csv input shape:
        Region,A,B,C,D
        North,1,2,3,4
        South,5,6,7,8
        '''
        # Initialize a dictionary for each column,
        # exclude the first column that has "Region" as header
        # Create a dictionary object from all the CSV file rows
        csv_reader = csv.DictReader(csv_file)

        # Collect all region values from the first column of the CSV file,
        # into the regions list.
        for row in csv_reader:
            regions.append(row[next(iter(row))])

        # After reading the regions reset the file pointer to the beginning of the file.
        csv_file.seek(0)
        # Skip the header row.
        next(csv_reader)

        # Iterate through each row of the CSV file loaded as csv_file.
        # Process the data to create a structured dictionary
        # to map activities to the values at each region.

        # Loop over each row in the CSV file. 
        # Use enumerate() to keep track of the current row index (i) and its content (row).
        # 
        for i, row in enumerate(csv_reader):
            # Inside the first loop, iterate over the column headers located in the first row.
            # To get these headers use the csv.DictReader() fieldnames method.
            # Start from the second element of the csv_reader.fieldnames array
            # to remove the first column header "Region".
            # The objective is to map activities to their values across different regions.
            for activity in csv_reader.fieldnames[1:]:
                # Meanwhile iterating over the rows,
                # check inside the second loop if the current column header (activity header) 
                # is not already a key in the activities = {} dictionary.
                # The activities = {} dictionary will store the activities as keys,
                # with a dictionary as their values, mapping regions to their respective values for that activity.
                if activity not in activities:
                    # If the activity is not a key in the activities dictionary,
                    # initialize a new dictionary for that activity.
                    # As an inner dictionary, each will map regions to values for that activity.
                    activities[activity] = {}
                # Use the stored region value instead of trying to access a removed column 'Region'
                # For each row update the inner dictionary for the current activity,
                # with a new key:value pair
                # The key will be the region name, originally from the "Region" column but retrieved from the regions = [] list using the current row index (i).
                # Assume regions = [] list has been already populated with regions names, maintaining the order they have at the CSV file.
                # The value will be the activity value for that region, retrieved from the current row --> row[activity]
                # At --> row[activity], activity is the current column header.
                # Coerce the value to a float because values have to be float numeric
                # activities[activity][row['Region']] = float(row[activity])
                activities[activity][regions[i]] = float(row[activity])


    # Convert the activities dictionary to a list of dictionaries.
    activities_list = [{activity: regions} for activity, regions in activities.items()]

   

    # Open the output json file, write.
    # If it exists, overwrite. If not, create with same name as the input file but with json extension.
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        # Write the final json object structure to the output json file.
        # dump() writes the json object to a file. Use indent 4.
        json.dump(activities_list, json_file, indent=4)       



# Call the function: input csv file, output json file
csv_to_json(csv_file_path, json_file_path)