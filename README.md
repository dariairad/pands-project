## pands-project

#### Author
Daria Sep (G00411221@gmit.ie)
#### Course
Higher Diploma in Computing in Data Analytics
#### Module
52167 - Programming and Scripting
#### Lecturer
Andrew Beatty (andrew.beatty@gmit.ie)

## Overview

This repository is a submission to Final Project for the Programming and Scripting module. The aim of this project is to investigate how Python can be utilized in order to carry out data analysis on the Fisher's Iris data set.

The repository contains

1. 1 x .py file
2. 1 x .data file
3. 1 x .md file 
4. 1 x .txt.file
5. 11 x .png file

The purpose of this README file is to provide insight into my process of researching and writing the code for those tasks.

## Fisher's Iris Data Set

#### History and Overview

![Figure1](https://machinelearninghd.com/wp-content/uploads/2021/03/iris-dataset.png)

## Libraries & Modules

```
import numpy as np
import matplotlib.pyplot as plt
import pandas as pnd 
import seaborn as sea
import sys 

```

1. `numpy` - NumPy is a Python library used for working with arrays.
2. `matplotlib`- Matplotlib is a data visualization and graphical plotting library for Python and its numerical extension NumPy.
3. `pandas` - Pandas is a Python library used for working with data sets (analyzing, cleaning, exploring, and manipulating data).
4. `seaborn` - Seaborn is a Python library built on top of matplotlib used for data visualization and exploratory data analysis.
5. `sys` - Sys provides functions and modules to interact with Python Interpreter. 


### Dataset

#### Dataset Import

```
file = 'iris.data' 
data = pnd.read_csv(file, header =None)
```

#### Analysis Summary of the Data

##### Number of Rows and Columns

```
print('\nNumber of Rows and Columns\n')
shape =(data.shape)
print (f'Rows: {shape[0]}')
print (f'Columns: {shape[1]}')
```

Number of Instances: 150 (50 in each of three classes)
Number of Attributes: 4 numeric, predictive attributes and the class

Attribute Information:
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm
   5. class: 
      - Iris Setosa
      - Iris Versicolour
      - Iris Virginica

Missing Attribute Values: None


Class Distribution: 33.3% for each of 3 classes.

## Histograms

### Code

Blah blah

### Histograms

blah blah

## Scatter Plots

### Code

### Scatter Plots

## Pairplot

### Code

### Pairplot

## References

Banerjee, R. (2021) *How to use Seaborn for Data Visualization* https://www.section.io/engineering-education/seaborn-tutorial/
Fisher R.A. (1936) *Iris Data Set* https://archive.ics.uci.edu/ml/datasets/iris
Holtz, Y. (n.d) *Histogram with several variables with Seaborn* https://python-graph-gallery.com/25-histogram-with-several-variables-seaborn
Kashnitsky, Y. (2021) *Topic 1. Exploratory Data Analysis with Pandas.* https://www.kaggle.com/code/kashnitsky/topic-1-exploratory-data-analysis-with-pandas/notebook
Pandas (n.d.) *DataFrame.* https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
Pandey, P. (2019) *Getting more value from the Pandas’ value_counts()* https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6
Ranjan, S. (2020) *Python | Pandas dataframe.corr().* https://www.geeksforgeeks.org/python-pandas-dataframe-corr/
Solomon, B. (2018) *Python Histogram Plotting: NumPy, Matplotlib, Pandas & Seaborn.* https://realpython.com/python-histograms/
Souveek (2021) *Python statistics | mean() function.* https://www.geeksforgeeks.org/python-statistics-mean-function/
StockOverflow (2019) *Append a Header for CSV file?* https://stackoverflow.com/questions/28162358/append-a-header-for-csv-file/28162530#28162530
StockOverflow (2020) *What are the arguments of seaborn's distplot used for?* https://stackoverflow.com/questions/56707800/what-are-the-arguments-of-seaborns-distplot-used-for
Stopak, J (2021) *Writing to a File with Python's print() Function* https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
The Matplotlib Development Team (n.p.). *matplotlib.pyplot* https://matplotlib.org/stable/api/pyplot_summary.html
W3Schools (n.p.). *Matplotlib Plotting.* https://www.w3schools.com/python/matplotlib_plotting.asp
W3Schools (n.p). *Pandas - Analyzing DataFrames.* https://www.w3schools.com/python/pandas/pandas_analyzing.asp
W3Schools (n.p). *Seaborn.* https://www.w3schools.com/python/numpy/numpy_random_seaborn.asp
Waskom, M. (n.d) *seaborn.histplot* https://seaborn.pydata.org/generated/seaborn.histplot.html
