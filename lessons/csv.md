# CSV (Comma separated values)

[csv official documentation](https://docs.python.org/3/library/csv.html)
[other csv documentation](https://realpython.com/python-csv/)

## Parsing

Parsing a file is analyzing a file's content to correctly structure the data.

## df

`df` command prints the currently used disk pace with readable format.

## csv module

### Create csv files

Examples:

```python
import csv

list = [["key", "value" ], ["key2", "value2"]]
with open("file.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(list)
```

### Read csv files

Examples:

```python
import csv

file = open("file.txt")
csv_file = csv.reader(file)
for row in csv_file:
    attribute_1, attribute_2, attribute_3 = row
    print(f'{attribute_1}, {attribute_2}, {attribute_3}')
file.close()
```

### Read and write csv files with Dictionaries

##### .DictReader()

Examples:

```python
import csv

with open("file.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f'{row[first_row]} | {row{second_row}}')
```

#### .DictWriter()

Examples:

```python
import csv

dictionary = [{"key1": "value1"}, {"key2": "value2"}, {"key3": "value3"}]
keys = ["key1", "key2", "key3"]
with open("file.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    wrier.writerows(dictionary)
```
