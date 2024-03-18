import csv

devices = []

with open('device_list.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        devices.append(lines[4])

file = open("devices", "w")
for device in devices[1:]:
    file.write(device + ":")
    file.write("\n")
file.close()