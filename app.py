print("Hello World")

import pandas as pd 
data_frame=pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame)

ages = [23,45,7,34,6,63,36,78,54,34]
print(pd.Series(ages))

a=pd.date_range(start="05/01/2021",end="05/12/2021",freq="D")
print(a)

my_series = pd.Series([2, 4, 6, 8, 10])
print(my_series.apply(lambda x:x/2))

data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porche", "Cayenne", "White"]]
print(pd.DataFrame(data,columns=["Brand", "Make", "Color"]))

data = [
    { 
        "brand": "Toyota", 
        "make": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "make": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porche", 
        "make": "Cayenne",
        "color": "White"
    },
    {
        "brand": "Tesla", 
        "make": "model S",
        "color": "Red"
    }
]
print(pd.DataFrame(data))

print(data_frame.iloc[133,6])

print(data_frame.head(3))
print(data_frame.tail(3))

print(data_frame.loc[0:4, ['Name', 'Type 1','Type 2']])

print(data_frame.loc[data_frame["Attack"]>80])

print(len(data_frame.loc[data_frame["Legendary"]==True]))

ex6=pd.read_csv('.learn/assets/us_baby_names_right.csv')
print(ex6.head())
j=ex6.iloc [:, 1:]
print(j.head())

print(ex6["Gender"].value_counts())
print(len(j.groupby(["Name"]).sum()))
print((j.groupby(["Name"]).sum()))