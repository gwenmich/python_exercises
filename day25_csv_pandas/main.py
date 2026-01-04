import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
#
# max_temp = data["temp"].max()
# # print(data[data.temp == max_temp])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# print(monday_temp[1])

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

squirrels_dict = {
    "Fur Colour" : ["grey", "red", "black"],
    "Count" : [grey_squirrels, red_squirrels, black_squirrels]
}

squirrel_data = pandas.DataFrame(squirrels_dict)
# squirrel_data.to_csv("squirrel_count.csv")

