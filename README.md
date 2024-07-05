# csv_json_scripts
# Utility script for converting and reshaping a CSV file with specific shape format to a output a JSON file with a required shape format.

Python scripts to convert csv to json, to a certain hierarchy shape.

Viceversa (TBA)

This script is for an specific shape of csv file to be converted to json of a specific shape.

Expected shape of the csv input file:

```
Region,A,B,C,D
North,1,2,3,4
South,5,6,7,8
```

"Region" item will not be included in the json output.

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

