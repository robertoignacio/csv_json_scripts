# csv_json_scripts
# Utility scripts when dealing with csv and json files
<br>
Python scripts to convert csv to json, to a certain hierarchy shape
Viceversa (TBA)
<br>
This script is for an specific shape of csv file to be converted to json of a specific shape.
<br>
Expected shape of the csv input file:
<br>
```
Region,A,B,C,D
North,1,2,3,4
South,5,6,7,8
```
<br>
To be converted to json, specified shape, as:
```
[
    {
        "A": {
        "North": 1,
        "South": 5,
        "East": 9,
        "West": 13
        }
    },
    {
        "B": {
        "North": 2,
        "South": 6,
        "East": 10,
        "West": 14
        }
    },
]
```
<br>
"Region" item will not be included in the json output.