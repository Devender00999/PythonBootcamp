# reading csv file without any library
# with open('./weather_data.csv') as file:
#    data = file.readlines()
#    print(data)
   
# reading csv file with built-in library 
# import csv
# with open('./weather_data.csv') as file:
#    data = csv.reader(file)
#    tempratures = []
#    for row in data:
#       if row[1] != "temp":
#          tempratures.append(int(row[1]))
#    print(tempratures)

# reading csv file with pandas
import pandas
data = pandas.read_csv('weather_data.csv')
print(data['temp'])


