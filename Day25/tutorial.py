import math
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
# data = pandas.read_csv('weather_data.csv')

# dataframe
# multi dimension array in pandas

# series 
# 1D Array

# print( data['temp'].min())

# get data in row
# print(data[data.temp == data.temp.max()])

# creating datafram from scratch
# data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "score": [76, 56, 65]
# }

# Saving data to csv
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')
# print(data.to_json())



squirrel_data = pandas.read_csv("squirrel.csv")
gray_sq_count= len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
cinnamon_sq_count= len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
black_sq_count= len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])

print(gray_sq_count, cinnamon_sq_count, black_sq_count)

data_dict = {
   "color": [ "gray", "cinnamon", 'black'],
   "count": [gray_sq_count, cinnamon_sq_count, black_sq_count]
}

pandas.DataFrame(data_dict).to_csv('squirrels_count.csv')




