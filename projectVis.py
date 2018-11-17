import csv
import datetime

with open('InputData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader)
    for row in reader:
        print(row)
        # if row['Colour'] == 'blue':
        #     print(row['ID'] ,row ['Make'],row ['Colour']





