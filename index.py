import csv

with open("file_name.csv") as file_name:
    file_read = csv.reader(file_name)
    array = list(file_read)
list = []
for x in array:
  inner = []
  for index,y in enumerate(x[0]):
    txt = x[0][:index] + ' ' + x[0][index:]
    inner.append(txt)
  list.append(inner)
    
f = open('new_file_name.csv', 'w')

# create the csv writer
writer = csv.writer(f,delimiter = "|")

# write a row to the csv file
writer.writerows(list)

# close the file
f.close()