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

# setting variables for atributes and class
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

def histogram_plot(p1, p2, p3):
    
    sea.histplot(data = iris_virginica[p1], color = 'dodgerblue') 
    sea.histplot(data = iris_versicolor[p1], color = 'mediumorchid')
    sea.histplot(data = iris_setosa[p1], color = 'teal')
    plt.xlabel(p2)
    plt.ylabel('Count')
    plt.title('Histogram of ' + p2 + ' by Species') 
    plt.legend(['Iris-virginica', 'Iris-versicolor', 'Iris_setosa'])
    plt.show()

def histograms():
    histogram_plot(sl, sl, 'sepal_length_by_species') 
    histogram_plot(sw, sw, 'sepal_width_by_species')
    histogram_plot(pl, pl, 'petal_length_by_species')
    histogram_plot(pw, pw, 'petal_width_by_species')

histograms()
plt.show()
