import csv
 
# data = "something"

# data = ["something"]

# data = ['one','two']

# data = [['something']]

data = [["Brand", "model", "type"],
          ['Hyudai', 'sedan', 'Petrol'],
          ['Honda', 'sedan', 'Diesel']]


file_opener = open('myfile.csv', 'w')

with file_opener:
    writer = csv.writer(file_opener)
    writer.writerows(data)
     
print "completed !"