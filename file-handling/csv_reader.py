import csv

file_opener = open('myfile.csv', 'r')

reader = csv.reader(file_opener)

for data in reader:
	print data