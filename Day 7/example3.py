import csv
with open("D:\Company_Data.csv","r")as file:
    csv_file=csv.reader(file)
    for lines in csv_file:
        print(lines)