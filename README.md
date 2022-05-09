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


## Dataset Import and Set up

#### Dataset Import

Code:

```
file = 'iris.data' 
data = pnd.read_csv(file, header =None)
```

#### Variables Set Up

Code:

```
sl = 'Sepal Length'
sw = 'Sepal Width'
pl = 'Petal Length'
pw = 'Petal Width'
sp = 'Species'

iris.columns = [sl, sw, pl, pw, sp]

iris_setosa = iris[iris[sp]=='Iris-setosa'] 
iris_virginica = iris[iris[sp]=='Iris-virginica']
iris_versicolor = iris[iris[sp]=='Iris-versicolor'] 

pal = ("dodgerblue", "mediumorchid", "teal", "slateblue")
sea.set(style="darkgrid", palette=pal)
```

Comments:

1. I set up variables for attributes and class for ease of use. 
2. Assigned column names. 
3. Grouped data by species.
4. Set up colour pallette and grid style for later plotting.

#### Redirecting Output

Code:

```
original_stdout = sys.stdout

with open("irisSummary.txt", "a") as f: 

    sys.stdout = f
    [...]
    sys.stdout = original_stdout
```
    
Comments: 
1. In order to save the output to a text file, I opened the file in the append mode and decided to import `sys` module to temporary redirect output from terminal to the file. 
2. Once, all the print commands were executed, the output had been set back to normal. 

## Analysis of the Iris Data Set

#### Data Overview

Code:

```
print(iris.head()) 
[...]
print (iris.sample(5))
```

Comments: 
In order to  ensure better understanding and provide an overview of the data set structure I decided to pull first 5 lines of the data set as well as a sample of 5 random entries. 

#### Basic Information

Code:

```
print (iris.info())
```

Comments: 
Code returns basic overview of the data incl. number of entries, number and names of columns, type of data, and Null valueas.

Data Insights:
1. Data set does not inlcude any Null values. 
2. There are 4 collumns of numeric and one class column. 
3. There's a total of 150 entries. 

#### Unique Species Names and Dataset Balance

Code:

```
print(iris[sp].value_counts())
[...]
print (iris[iris.duplicated()])
```

Comments:
1. `iris[sp]` returns a list of all instances of species. By using `value_count()`, the instances are grouped and counted, and returned as a sum value grouped by species. 
2. `iris.duplicated()` searches for duplicate entries. 

Data Insights:
1. There are 3 types of species, each comes up 50 times. Therefore, this dataset is of a balnced type. 
2.  There's 1 duplicate entry in the data set. However we should not remove as it would cause an inbalance in the data set. 


#### Statistical Insights and Further Analysis

Code:

```
print(iris.describe())
[...]
print(iris.median()) 
[...]
print(iris.groupby(sp).mean())
[...]
print(iris.groupby(sp).corr())
```

Data Insights: 
1. Mean Values
2. Standard Deviation
3. Minimum Values
4. Maximum Values
5. Median Values by Species
6. Correlation Between Attributes

## Data Visualisation

#### Species Count 

Code:

```
plt.title('Species Count')
sea.countplot(x=sp, data=iris)
plt.savefig('species_count')
```

Output:

![Figure2](https://raw.githubusercontent.com/dariairad/pands-project/main/species_count.png)

#### Attributes Count 

Code: 

```
fig, axs = plt.subplots(2, 2, figsize=(8, 8))
sea.histplot(data=iris, x=sl, color="dodgerblue", ax=axs[0, 0])
sea.histplot(data=iris, x=sw, color="mediumorchid", ax=axs[0, 1])
sea.histplot(data=iris, x=pl, color="slateblue", ax=axs[1, 0])
sea.histplot(data=iris, x=pw, color="teal", ax=axs[1, 1])
plt.suptitle('Attributes - General')
plt.savefig('attributes_general')
```

Output:

![Figure3](https://github.com/dariairad/pands-project/blob/main/attributes_general.png)


#### Attributes by Species

Code:

```
def histogram_plot(p1, p2, p3):   
    sea.histplot(data = iris_virginica[p1], label = 'Iris virginica', color = 'dodgerblue') 
    sea.histplot(data = iris_versicolor[p1], label = 'Iris versicolor', color = 'mediumorchid')
    sea.histplot(data = iris_setosa[p1], label = 'Iris setosa', color = 'teal')
    plt.xlabel(p2)
    plt.ylabel('Count')
    plt.title('Histogram of ' + p2 + ' by Species') 
    plt.legend(['Iris-virginica', 'Iris-versicolor', 'Iris_setosa'])
    plt.savefig(p3)

def histograms():
    histogram_plot(sl, sl, 'sepal_length_by_species') 
    histogram_plot(sw, sw, 'sepal_width_by_species')
    histogram_plot(pl, pl, 'petal_length_by_species')
    histogram_plot(pw, pw, 'petal_width_by_species')

histograms()
```

Output:

![Figure4](https://raw.githubusercontent.com/dariairad/pands-project/main/petal_length_by_species.png)

![Figure5](https://raw.githubusercontent.com/dariairad/pands-project/main/petal_width_by_species.png)

![Figure6](https://raw.githubusercontent.com/dariairad/pands-project/main/sepal_length_by_species.png)

![Figure7](https://raw.githubusercontent.com/dariairad/pands-project/main/sepal_width_by_species.png)

#### Attribiutes by Species + Outliers

Code: 

```
fig, axes = plt.subplots(2, 2, figsize=(8, 8)) 
sea.boxplot(x=sp, y=pl,data=iris, ax=axes[0,0])
sea.boxplot(x=sp, y=sl, data=iris, ax=axes[0,1])
sea.boxplot(x=sp, y=pw,data=iris, ax=axes[1,0])
sea.boxplot(x=sp, y=sw, data=iris, ax=axes[1,1])
plt.suptitle('Attributes by Species + Outliers')
plt.legend()
plt.savefig('atributes_outliers')
```

Output:

![Figure8](https://raw.githubusercontent.com/dariairad/pands-project/main/atributes_outliers.png)

#### Correlation Between Atributes 

Code:

```
sea.scatterplot(x=pl, y=pw, hue=sp, data=iris, palette=pal)
plt.legend(loc='upper left')
plt.title('Correraltion between Petal Length & Width')
plt.savefig('petal_length_width')

sea.scatterplot(x=sl, y=sw, hue=sp, data=iris, palette=pal)
plt.legend(loc='upper right')
plt.title('Correraltion between Sepal Length & Width')
plt.savefig('sepal_length_width')
```

Output:

![Figure9](https://raw.githubusercontent.com/dariairad/pands-project/main/sepal_length_width.png)
![Figure10](https://raw.githubusercontent.com/dariairad/pands-project/main/petal_length_width.png)

#### Relationship Between Attributes by Species

Code:

```
sea.pairplot(data=iris, hue=sp, height=2, palette=pal)
plt.subplots_adjust(top=0.95)
plt.suptitle('Relationship Between Attributes by Species')
plt.savefig('attributes_pairplot')
```

Output:

![Figure11](https://raw.githubusercontent.com/dariairad/pands-project/main/attributes_pairplot.png)



## References

1. Banerjee, R. (2021) *How to use Seaborn for Data Visualization* https://www.section.io/engineering-education/seaborn-tutorial/
2. Fisher R.A. (1936) *Iris Data Set* https://archive.ics.uci.edu/ml/datasets/iris
3. Holtz, Y. (n.d) *Histogram with several variables with Seaborn* https://python-graph-gallery.com/25-histogram-with-several-variables-seaborn
4. Kashnitsky, Y. (2021) *Topic 1. Exploratory Data Analysis with Pandas.* https://www.kaggle.com/code/kashnitsky/topic-1-exploratory-data-analysis-with-pandas/notebook
5. Pandas (n.d.) *DataFrame.* https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
6. Pandey, P. (2019) *Getting more value from the Pandas’ value_counts()* https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6
7. Ranjan, S. (2020) *Python | Pandas dataframe.corr().* https://www.geeksforgeeks.org/python-pandas-dataframe-corr/
8. Solomon, B. (2018) *Python Histogram Plotting: NumPy, Matplotlib, Pandas & Seaborn.* https://realpython.com/python-histograms/
9. Souveek (2021) *Python statistics | mean() function.* https://www.geeksforgeeks.org/python-statistics-mean-function/
10. StockOverflow (2019) *Append a Header for CSV file?* https://stackoverflow.com/questions/28162358/append-a-header-for-csv-file/28162530#28162530
11. StockOverflow (2020) *What are the arguments of seaborn's distplot used for?* https://stackoverflow.com/questions/56707800/what-are-the-arguments-of-seaborns-distplot-used-for
12. Stopak, J (2021) *Writing to a File with Python's print() Function* https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
13. The Matplotlib Development Team (n.p.). *matplotlib.pyplot* https://matplotlib.org/stable/api/pyplot_summary.html
14. W3Schools (n.p.). *Matplotlib Plotting.* https://www.w3schools.com/python/matplotlib_plotting.asp
15. W3Schools (n.p). *Pandas - Analyzing DataFrames.* https://www.w3schools.com/python/pandas/pandas_analyzing.asp
16. W3Schools (n.p). *Seaborn.* https://www.w3schools.com/python/numpy/numpy_random_seaborn.asp#
17. Waskom, M. (n.d) *seaborn.histplot* https://seaborn.pydata.org/generated/seaborn.histplot.html
