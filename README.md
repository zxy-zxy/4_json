#Prettify JSON
Simple script that pretty prints JSON content of provided file.
## Usage
Python >= 3.5 required.
### Example use
To run script open linux shell and run pprint_json.py with required argument.
``` 
python pprint_json.py -filepath < your_filename_here.json >
```
Example output:
```
[
    {
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Number": 1,
        "Cells": {
            "global_id": 14371450,
            "Name": "Ароматный Мир",
            "IsNetObject": "да",
            "OperatingCompany": "Ароматный Мир",
            "TypeService": "реализация продовольственных товаров",
            "AdmArea": "Западный административный округ",
            "District": "район Кунцево",
            "Address": "улица Академика Павлова, дом 10",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ]
        }
    }
]
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
