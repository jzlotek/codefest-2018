import csv

def get_info():
    with open('hydrants.csv',newline='\n') as file:
        csvreader = csv.DictReader(file)
        return [row for row in csvreader]
