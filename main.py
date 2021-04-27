# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].tolist()
# print(temp_list)
#
# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# tem_in_c = int(monday.temp)
# tem_in_f = tem_in_c * 9 / 5 + 32
# print(tem_in_f)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")