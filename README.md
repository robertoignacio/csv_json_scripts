# Utility scripts for converting and reshaping a CSV file with specific shape format to a output a JSON file with a required shape format.

Python scripts to convert CSV to JSON, to a certain hierarchy shape.

Currently this repo contains only one script, but it is expected to grow with more scripts for different shapes.

## csv2jsontree.py
[csv2jsontree](scripts/csv2jsontree.py)

This script is for an specific shape of csv file to be converted to json of a specific shape.

(Review the script for the path route for the input and output files).

Expects this CSV file shape:

```
Region,Column A,Column B,Column C,Column D
North,1.1,1.2,1.3,1.4
South,1.5,1.6,1.7,1.8
```

"Region" item will not be included in the JSON file output shape.

JSON file required shape:

```
[
    {
        "Column A": {
        "North": "1.1%",
        "South": "1.5%",
        }
    },
    {
        "Column B": {
        "North": "1.2%",
        "South": "1.6%",
        }
    },
    {
        "Column C": {
        "North": "1.3%",
        "South": "1.7%",
        }
    },
    {
        "Column D": {
        "North": "1.4%",
        "South": "1.8%",
        }
    }
]
```