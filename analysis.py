# Analysis of Iris Dataset.
# Author: Daria Sep

import numpy as np
import matplotlib.pyplot as plt
import pandas as pnd 
import seaborn as sea

# Importing data from the file.

file = 'iris.data' 
data = pnd.read_csv(file, header =None)

#sea.set(style="whitegrid", rc={'figure.figsize':(10,6)}) 

data.columns = ['Sepal Length (cm)','Sepal Width (cm)','Petal Length (cm)','Petal Width (cm)','Species']
# Adding headers to columns

print('\nAnalysis of the Iris Dataset\n') 

print('\nOverview of the Dataset - First 5 and Last 5 Rows\n')
# Overview of the dataset in a table format
print(f'{data.head()}\n') 
print(data.tail())

print('\nSample of Data - 5 Random Entries\n')# Random sample of data from the dataset. 
sample = data.sample(5)
print(sample) # Outputs five random complete data entries from the dataset

print('\nNumber of Rows and Columns\n')
# Shape of the dataset (rows, columns)
shape =(data.shape)
print(f'Rows: {shape[0]}')
print(f'Columns: {shape[1]}')

print('\nUnique Species Names and Count\n')
print(data['Species'].value_counts())

print('\nNull Values\n')
print (data.isnull().sum())

print('\nStatistical Insights\n')
#The statistical insights
print(data.describe())

print('\nMedian of Attributes\n') 
print(data.median()) # Print the median of each of the attributes in tabular form

print('\nThe Mean Values of the Three Species\n')
print(data.groupby('Species').mean())
print('\nThe Correlation Between the Values of the Three Species\n')
print(data.groupby('Species').corr())



