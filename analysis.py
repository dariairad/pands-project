# Analysis of the Iris Dataset.
# Author: Daria Sep

import numpy as np
import matplotlib.pyplot as plt
import pandas as pnd
import seaborn as sea
import sys 

# Importing data from the file.
file1 = 'iris.data' 
iris = pnd.read_csv(file1, header =None)

# setting variables for attributes and class
sl = 'Sepal Length'
sw = 'Sepal Width'
pl = 'Petal Length'
pw = 'Petal Width'
sp = 'Species'

# Adding headers to columns
iris.columns = [sl, sw, pl, pw, sp]

# Categorizing data by species
iris_setosa = iris[iris[sp]=='Iris-setosa'] 
iris_virginica = iris[iris[sp]=='Iris-virginica']
iris_versicolor = iris[iris[sp]=='Iris-versicolor'] 

# setting style of the grid + colour palette
pal = ("dodgerblue", "mediumorchid", "teal", "slateblue")
sea.set(style="darkgrid", palette=pal)

original_stdout = sys.stdout

with open("irisSummary.txt", "a") as f: 

    sys.stdout = f
    print('\n************************ ANALYSIS OF THE IRIS DATASET *************************\n\n') 
    print ('============================== Basic information ==============================\n')
    print (iris.info()) 
    #Checking info on dataset: rows, columns, entries, data types, null values

    print('\n=================== Unique Species Names and Dataset Balance  ==================\n')
    print(iris[sp].value_counts())

    print ('\n=============================== Duplicate Entries ==============================\n')
    print (iris[iris.duplicated()])

    print('\n============================ Overview of the Dataset ==========================\n')
    print('------------------------------------- First 5 Rows ------------------------------\n')
    print(iris.head()) 
    print('\n------------------------- Random Sample - 5 Random Rows -------------------------\n')# Random sample of data from the dataset. 
    print (iris.sample(5))
    # Outputs five random complete data entries from the dataset

    print('\n============================= Statistical Insights =============================\n')
    #The statistical insights
    print(iris.describe())

    print('\n============================= Median of Attributes ===========================\n') 
    print(iris.median()) # Print the median of each of the attributes in tabular form

    print('\n====================== The Mean Values of the Three Species ======================\n')
    print(iris.groupby(sp).mean())
    print('\n============= The Correlation Between the Values of the Three Species ============\n')
    print(iris.groupby(sp).corr())

    sys.stdout = original_stdout

# Species count, further showing the balance of the data base

plt.title('Species Count')
sea.countplot(x=sp, data=iris)
plt.savefig('species_count')
plt.show()

# histogram - general by attribute
fig, axs = plt.subplots(2, 2, figsize=(8, 8))
sea.histplot(data=iris, x=sl, color="dodgerblue", ax=axs[0, 0])
sea.histplot(data=iris, x=sw, color="mediumorchid", ax=axs[0, 1])
sea.histplot(data=iris, x=pl, color="slateblue", ax=axs[1, 0])
sea.histplot(data=iris, x=pw, color="teal", ax=axs[1, 1])
plt.suptitle('Attributes - General')
plt.savefig('attributes_general')
plt.show()

# defining function for histograms - attributes by species
def histogram_plot(p1, p2, p3):
    
    sea.histplot(data = iris_virginica[p1], color = 'dodgerblue') 
    sea.histplot(data = iris_versicolor[p1], color = 'mediumorchid')
    sea.histplot(data = iris_setosa[p1], color = 'teal')
    plt.xlabel(p2)
    plt.ylabel('Count')
    plt.title('Histogram of ' + p2 + ' by Species') 
    plt.legend(['Iris-virginica', 'Iris-versicolor', 'Iris_setosa'])
    plt.savefig(p3)
    plt.show()

def histograms():
    histogram_plot(sl, sl, 'sepal_length_by_species') 
    histogram_plot(sw, sw, 'sepal_width_by_species')
    histogram_plot(pl, pl, 'petal_length_by_species')
    histogram_plot(pw, pw, 'petal_width_by_species')

histograms()
plt.show()

# Attributes by species + Outliers
fig, axes = plt.subplots(2, 2, figsize=(8, 8)) 
sea.boxplot(x=sp, y=pl,data=iris, ax=axes[0,0])
sea.boxplot(x=sp, y=sl, data=iris, ax=axes[0,1])
sea.boxplot(x=sp, y=pw,data=iris, ax=axes[1,0])
sea.boxplot(x=sp, y=sw, data=iris, ax=axes[1,1])
plt.suptitle('Attributes by Species + Outliers')
plt.legend()
plt.savefig('attributes_outliers')
plt.show()

sea.scatterplot(x=pl, y=pw, hue=sp, data=iris, palette=pal)
plt.legend(loc='upper left')
plt.title('Correlation between Petal Length & Width')
plt.savefig('petal_length_width')
plt.show()

sea.scatterplot(x=sl, y=sw, hue=sp, data=iris, palette=pal)
plt.legend(loc='upper right')
plt.title('Correlation between Sepal Length & Width')
plt.savefig('sepal_length_width')
plt.show()

sea.pairplot(data=iris, hue=sp, height=2, palette=pal)
plt.subplots_adjust(top=0.95)
plt.suptitle('Relationship Between Attributes by Species')
plt.savefig('attributes_pairplot')
plt.show()
