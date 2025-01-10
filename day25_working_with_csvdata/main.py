
# with open("weather_data.csv") as data_file:
#     datas = data_file.readlines()
#     print(datas)

# import csv
# with open("weather_data.csv") as data_file:
#     data_obj = csv.reader(data_file)
#     temperatures = []
#     for row in data_obj:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# Get data Column
# print(data["condition"])
# print(data.condition)

# Get data row
# print(data[data.day == "Monday"])

# Row of data which had the highest temperature
# print(data[data.temp == data.temp.max()])

# Convert Monday's temperature to Fahrenheit
# monday_row = data[data.day == "Monday"]
# print(monday_row)
# print(monday_row.temp)
# Fah = (Celsius * 1.8) + 32

# monday_temp_fah = (monday_row.temp[0] * 1.8) + 32
# print(f"Monday Temp: {monday_temp_fah} F")


# Create a data Frame from scratch
# data_dict = {
#     "student": ["Army", "James", "Angela"],
#     "scores": [76,57,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("score_data.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250109.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinna_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "fur color" : ["Gray", "Cinnamon","Black"],
    "count":[gray_squirrel_count, cinna_squirrel_count, black_squirrel_count]
}

df_squirrel = pandas.DataFrame(data_dict)
df_squirrel.to_csv("squirrel_count.csv")



