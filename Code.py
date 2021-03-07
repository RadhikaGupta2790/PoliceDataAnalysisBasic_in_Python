"""
@author: shell
"""
#DATA SET LINK IN README



import pandas as pd
#IMPORTING DATA
data=pd.read_csv(r"C:\Users\shell\OneDrive\Desktop\SOFTWARE TOOLS\Police Data.csv")

#removing column that contains only null values
data.isnull().sum() # for particular column total no. of null occurence
data.drop(columns ="country_name", inplace=True) 

"""FOR SPEEDING WERE MEN OR WOMEN STOPPED MORE OFTEN?"""
#for pie chart
data[data.violation =="Speeding"].driver_gender.value_counts().plot.pie(subplots=True)
#for numbers
print("no.of males and females stopped for speeding:")
print(data[data.violation =="Speeding"].driver_gender.value_counts())

"""DOES GENDER EFFECT WHO GETS SEARCHED DURING A STOP?"""
#TOTAL NO. OF TIMES SEARCH WAS CONDUCTED
print(data.search_conducted.value_counts())
#as search conductedARE 2479 so no of male and females will be out of 2479
print("no.of males and females searched during a stop:")
print(data.groupby('driver_gender').search_conducted.sum())


"""WHAT IS MEAN OF STOP DURATION"""
print(data.stop_duration.value_counts())
data['stop_duration']=data['stop_duration'].map({'0-15 Min': 7.5,'16-30 Min': 24, '30+ Min': 45 })
print("mean of stop duration:")
print(data['stop_duration'].mean())


print(data.groupby('violation').driver_age.describe())

