# -*- coding: utf-8 -*-
"""Classification - AirBnB Amsterdam Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zSuaLQgy3JsTwaPhajpEFRV73FN1FGuA
"""

#import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('airbnb_amsterdam.xlsx')         #declare variable df to read excel file
df                                                  #showing the data

df.isnull().sum()                   #finding out missing values

df = pd.read_excel('airbnb_amsterdam.xlsx')       #declare variable df to read excel file
df [['bedrooms','guests_included']][0:14]         #showing the columns 'bedrooms' & 'guests_include' from row 1-14

df1 = pd.read_excel('airbnb_amsterdam.xlsx')              #declare variable df1 to read excel file
df1['price_category'].value_counts()                      #count the values of 'price_category' as class/labels

plt.figure(figsize=(8,8))                                         #size of pie chart
exp=[0.05,0,0,0]                                                  #declare variable exp
color = ['#ff0000','#ff5252','#ff7b7b','#ffbaba']                 #declare variable color
df1 = pd.read_excel('airbnb_amsterdam.xlsx')                      #declare variable df1
values = df1['price_category'].value_counts()                     #declare variable values
plt.title("Price Category")                                       #title name of pie chart
#set up the pie chart
plt.pie(df['price_category'].value_counts(),                      #input column for pie chart values
        labels=df['price_category'].value_counts().index,         #naming labels 
        autopct=lambda p:f'{p:.2f}%, ({p*sum(values)/100 :.0f})', #input percentages & numbers for values
        explode = exp,                                            #range for each slices of pie chart
        colors=color);                                            #colors for pie chart
plt.show()                                                        #syntax for show the pie chart

df3 = pd.read_excel('airbnb_amsterdam.xlsx')          #declare variable df3 to read excel file
df3['accommodates'].max()                             #finding out max values from 'accommadates' column

df4 = pd.read_excel('airbnb_amsterdam.xlsx')          #declare variable df4 to read excel file
bedrooms = df4['bedrooms']                            #declare variable bedrooms
#showing the list of 'accommodates' data, when the 'bedrooms' values was 3
df4.groupby('bedrooms')['accommodates'].value_counts().loc[lambda x : 3]

#showing sum of 'accommodates' data, when the 'bedrooms' values was 3
bedrooms.value_counts().loc[lambda x : 3]

#preprocessing data
from sklearn.preprocessing import LabelEncoder                #import for label encoding
df5 = pd.read_excel('airbnb_amsterdam.xlsx')                  #declare variable df5 to read excel file
df5 = df5.drop(columns=['host_listings_count',                #dropping useless columns
                        'calculated_host_listings_count',
                        'latitude',
                        'longitude',
                        'instant_bookable_t',
                        'room_type_Entire home/apt',
                        'room_type_Private room',
                        'room_type_Shared room'])
df5 = df5.apply(LabelEncoder().fit_transform)                 #applying encoder data
df5

df5['price_category'].value_counts()

#define training & testing data
from sklearn.model_selection import train_test_split

features = df5.iloc[:,0:7]                            #set the column you want to display
label = df5.iloc[:,7]                                 #set the column that will be the labels

x_train, x_test, y_train, y_test = train_test_split(  
    features, label,                                  #set x values & y values
    test_size = 0.10,                                 #set the percentage data you want to use
    random_state = 42
    )
x_test                                                #show x test

#create and apply the model
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model = model.fit(x_train, y_train)

#from sklearn.tree import DecisionTreeClassifier
#model = DecisionTreeClassifier()
#model = model.fit(x_train, y_train)

print(model.predict(x_test))                      
print(y_test)                                   #show y test

#Calculate Accuracy Score
from sklearn.metrics import accuracy_score
hasil_prediksi = model.predict(x_test)
accuracy_score(y_test, hasil_prediksi)

#Create Confusion Matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(hasil_prediksi, y_test)

#Create Classification Report
from sklearn.metrics import classification_report
print(classification_report( y_test, hasil_prediksi))