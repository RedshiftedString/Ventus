import csv

with open("sensorDataConverted.csv", 'r') as sensorData:
    for i, line in enumerate(sensorData):
        print(i, line)
        