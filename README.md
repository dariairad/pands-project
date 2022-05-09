## pands-project

#### Author
Daria Sep (G00411221@gmit.ie)
#### Course
Higher Diploma in Computing in Data Analytics
#### Module
52167 - Programming and Scripting
#### Lecturer
Andrew Beatty (andrew.beatty@gmit.ie)

### Overview

This repository is a submission of the Final Project for the Programming and Scripting module. The aim of this project is to investigate how Python can be utilized in order to carry out data analysis on the Fisher's Iris data set.

The repository contains:

1. 1 x .py file
2. 1 x .data file
3. 1 x .md file 
4. 1 x .txt.file
5. 11 x .png file

The purpose of this README file is to provide insight into my process of researching and writing the code for this project.

## Fisher's Iris Data Set

### History

The Iris Dataset, aslo known as the Fisher's Iris Dataset, is a multivariate dataset created by Sir Ronald Aymer Fisher in 1936. 

![Figure13](https://upload.wikimedia.org/wikipedia/commons/a/aa/Youngronaldfisher2.JPG)

It is also sometimes referred to as Anderson’s Iris data set as Edge Anderson originally collected the data to quantify the variation of Iris flowers of three different class.

The dataset was originally used as an example of linear discrimination analysis. However, it later became used as a test case for statistical classification techniques in machine learning. The Iris Data Set is now widely used as a beginner's dataset for machine learning purposes.

### Dataset Description

The information that is included in the dataset is as follows:

1. Sepal length in cm
2. Sepal width in cm
3. Petal length in cm
4. Petal width in cm
5. Class:
    - Iris Setosa
    - Iris Versicolour
    - Iris Virginica

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

### Dataset Import

#### Code

```
file = 'iris.data' 
data = pnd.read_csv(file, header =None)
```

### Variables Set Up

#### Code

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

#### Comments

1. I set up variables for attributes and class for ease of use. 
2. Assigned column names. 
3. Grouped data by species.
4. Set up colour pallette and grid style for later plotting.

### Redirecting Output

#### Code

```
original_stdout = sys.stdout

with open("irisSummary.txt", "a") as f: 

    sys.stdout = f
    [...]
    sys.stdout = original_stdout
```
    
#### Comments

1. In order to save the output to a text file, I opened the file in the append mode and decided to import the sys module to temporarily redirect output from the terminal to a file.
2. Once all the print commands were executed, the output had been set back to normal.

## Analysis of the Iris Data Set

### Data Overview

#### Code

```
print(iris.head()) 
[...]
print (iris.sample(5))
```

#### Comments

In order to  ensure better understanding and provide an overview of the data set structure I decided to pull the first 5 lines of the data set as well as a sample of 5 random entries. 

### Basic Information

#### Code

```
print (iris.info())
```

#### Comments

Code returns basic overview of the data incl. number of entries, number and names of columns, type of data, and Null values.

#### Data Insights

1. Data set does not include any Null values.
2. There are 4 columns of numeric values and one class column.
3. There's a total of 150 data entries. 

### Unique Species Names and Dataset Balance

#### Code

```
print(iris[sp].value_counts())
[...]
print (iris[iris.duplicated()])
```

#### Comments

1. `iris[sp]` returns a list of all instances of species. By using `value_count()`, the instances are grouped and counted, and returned as a sum value grouped by species. 
2. `iris.duplicated()` searches for duplicate entries. 

#### Data Insights

1. There are 3 types of species, each comes up 50 times. Therefore, this dataset is of a balanced type. 
2. There's 1 duplicate entry in the data set. However we should not remove as it would cause an imbalance in the data set. 


### Statistical Insights and Further Analysis

#### Code

```
print(iris.describe())
[...]
print(iris.median()) 
[...]
print(iris.groupby(sp).mean())
[...]
print(iris.groupby(sp).corr())
```

#### Data Insights

1. Mean Values
2. Standard Deviation
3. Minimum Values
4. Maximum Values
5. Median Values by Species
6. Correlation Between Attributes

## Data Visualisation

### Species Count 

#### Code

```
plt.title('Species Count')
sea.countplot(x=sp, data=iris)
plt.savefig('species_count')
plt.close()
```

#### Comments

1. `plt.title()` lets us pass a string to se the title for the plot.
2. `sea.countplot()` grups and sums the values as chosen. This function takes multiple arguments. Here we have the x axis set to species thus the data gets grouped by species, and the iris Database under data. 
3. `plt.savefigure()` saves the image of the plot to a specified file. 
4. `plt.close()` closes the plot after execution. 

#### Output

![Figure2](https://raw.githubusercontent.com/dariairad/pands-project/main/species_count.png)

#### Data Insights:

The plot further demonstrates this is a balanced database.

### Attributes Count 

#### Code

```
fig, axs = plt.subplots(2, 2, figsize=(16, 9))
sea.histplot(data=iris, x=sl, color="dodgerblue", ax=axs[0, 0], bins=7)
sea.histplot(data=iris, x=sw, color="mediumorchid", ax=axs[0, 1], bins=5)
sea.histplot(data=iris, x=pl, color="slateblue", ax=axs[1, 0], bins=7)
sea.histplot(data=iris, x=pw, color="teal", ax=axs[1, 1], bins=5)
plt.suptitle('Attributes - General')
plt.savefig('attributes_general')
plt.close()
```

#### Comments

1. I started with setting the plots parameters then created 4 histographs using `sea.histplot()`
2. `sea.histplot()` takes in multiple arguments that allow us to manipulate the information included in the histogram as well as the plot's visual attributes.
3. I have used following arguments: 
    - data - the Iris Dataset
    - x axis - attributes from the database (petal width and height, sepal width and length)
    - color 
    - ax - to organise the multiple plots on one image
    - bins - to set the number of bars
4. `plt.suptitle()` allows us to assign a title to an entire set rather than single plot. 
5. `plt.savefig()` and `plt.close()` saves the plot to a png file and exits out after executio respectively. I will ommit these in the further comments as they are used in all plots along with `plt.title()` and/or `plt.suptitle()`.

#### Output

![Figure3](https://raw.githubusercontent.com/dariairad/pands-project/main/attributes_general.png)

#### Data Insights:

The plot gives an overview of a general distribution of the attributes in the database as a whole. From the plot we can observe that:

1. The most common sepal length is between 5.5 and 6.0, total of 34 entries.
2. The most common sepal width is between 3.0 to 3.5, total of around 68 entries.
3. The most common petal length is between 1 to 2, total of around 48.
4. The most common petal width is between 0 to 0.5, total of 49.

### Correlation Between Attributes

#### Code

```
plt.figure(figsize=(8,8))
sea.heatmap(iris.corr(), annot=True, cmap='Blues')
plt.title('Correlation Between Attributes')
plt.savefig('heatmap')
plt.close()
```

#### Comments

1. I set figure parameters. 
2. Then generated a heat map of correlations between attributes using `sea.heatmap()`.
3. Arguments passed are as follows:
    - `iris.corr()` function that analyses the correlations
    - annot - let's us choose whether annotations should be included on the heatmap
    - cmap - to set the color palette for the heatmap 

#### Output

![Figure12](https://raw.githubusercontent.com/dariairad/pands-project/main/heatmap.png)


### Attributes by Species

#### Code

```
def histogram_plot(p1, p2, p3):   
    sea.histplot(data = iris_virginica[p1], color = 'dodgerblue') 
    sea.histplot(data = iris_versicolor[p1], color = 'mediumorchid')
    sea.histplot(data = iris_setosa[p1], color = 'teal')
    plt.xlabel(p2)
    plt.ylabel('Count')
    plt.title('Histogram of ' + p2 + ' by Species') 
    plt.legend(['Iris-virginica', 'Iris-versicolor', 'Iris_setosa'])
    plt.savefig(p3)
    plt.close()

def histograms():
    histogram_plot(sl, sl, 'sepal_length_by_species') 
    histogram_plot(sw, sw, 'sepal_width_by_species')
    histogram_plot(pl, pl, 'petal_length_by_species')
    histogram_plot(pw, pw, 'petal_width_by_species')

histograms()
```

#### Comments

1. Here, we are creating 4 seperate histograms showing the attributes' frequency organised by species. 
2. I decided to create 2 functions rather than generating each histogram separately. 
3. Started with defining`histogram_plot()` function that includes the pattern of data inluded in each histogram as well as visual attributes:
    - `sea.histplot()` generates a histogram
    - `plt.xlabel()` and `plot.ylabel()` allows to set custom labeling for x and y axis respectively
    - `plt.legend()` adds legend box to a plot. It takes number of arguments allowing for set up of customised labels, title as well as manipulate the positioning of the legend box as seen further down.
4. The function takes in 3 arguments: attribute values, attribute name, and plot's title. 
5.  The arguments for each seperate histogram are listed under second function `histograms()`.
6.  After defining both functions, the function was executed resulting in 4 histograms being generate, as seen below. 

#### Output

![Figure4](https://raw.githubusercontent.com/dariairad/pands-project/main/sepal_width_by_species.png)

![Figure5](https://raw.githubusercontent.com/dariairad/pands-project/main/sepal_length_by_species.png)

![Figure6](https://raw.githubusercontent.com/dariairad/pands-project/main/petal_length_by_species.png)

![Figure7](https://raw.githubusercontent.com/dariairad/pands-project/main/petal_width_by_species.png)

#### Data Insights

1. There is a significant overlap between the species' sepal length, and even more prominent overlap between the species' sepal width. Therefore it's not an effective classification criteria.
2. Petal width and length is a much better classification feature as the overlap is minor, with Iris Setosa being fully separated from the other 2 species.

### Attributes by Species + Outliers

#### Code

```
fig, axes = plt.subplots(2, 2, figsize=(8, 8)) 
sea.boxplot(x=sp, y=pl,data=iris, ax=axes[0,0])
sea.boxplot(x=sp, y=sl, data=iris, ax=axes[0,1])
sea.boxplot(x=sp, y=pw,data=iris, ax=axes[1,0])
sea.boxplot(x=sp, y=sw, data=iris, ax=axes[1,1])
plt.suptitle('Attributes by Species + Outliers')
plt.legend()
plt.savefig('atributes_outliers')
plt.close()
```

#### Output

![Figure8](https://raw.githubusercontent.com/dariairad/pands-project/main/attributes_outliers.png)

#### Data Insights

1. Iris Setosa has smaller and less distributed features.
2. Iris Versicolor is distributed in an average manner.
3. Iris Virginica is highly distributed with large number of features.
4. Additionally, median and mean values are shown for each attribute and species. 

### Correlation Between Atributes by Species

#### Code

```
sea.scatterplot(x=pl, y=pw, hue=sp, data=iris, palette=pal)
plt.legend(loc='upper left')
plt.title('Correraltion between Petal Length & Width')
plt.savefig('petal_length_width')
plt.close()

sea.scatterplot(x=sl, y=sw, hue=sp, data=iris, palette=pal)
plt.legend(loc='upper right')
plt.title('Correraltion between Sepal Length & Width')
plt.savefig('sepal_length_width')
plt.close()
```

#### Output

![Figure9](https://raw.githubusercontent.com/dariairad/pands-project/main/sepal_length_width.png)
![Figure10](https://raw.githubusercontent.com/dariairad/pands-project/main/petal_length_width.png)

#### Data Insights

1. Iris Setosa species has smaller sepal length but relatively higher width.
   Iris Versicolor sepal lengths and witdths are almost at the middle of the spectrum.
   Iris Virginica has larger sepal lengths and smaller sepal widths than the rest.
2. Iris Setosa has the smallest petal length as well as petal width
   Iris Versicolor has average petal length and petal width
   Iris Virginica has the highest petal length as well as petal width

### Relationship Between Attributes by Species

#### Code

```
sea.pairplot(data=iris, hue=sp, height=2, palette=pal)
plt.subplots_adjust(top=0.95)
plt.suptitle('Relationship Between Attributes by Species')
plt.savefig('attributes_pairplot')
plt.close()
```

#### Output

![Figure11](https://raw.githubusercontent.com/dariairad/pands-project/main/attributes_pairplot.png)

## References

1. Banerjee, R. (2021) *How to use Seaborn for Data Visualization* https://www.section.io/engineering-education/seaborn-tutorial/
2. Fisher R.A. (1936) *Iris Data Set* https://archive.ics.uci.edu/ml/datasets/iris
3. Chauhan, G. (2021) 
4. Holtz, Y. (n.d) *Iris Dataset Project from UCI Machine Learning Repository* https://machinelearninghd.com/iris-dataset-uci-machine-learning-repository-project/
- *Histogram with several variables with Seaborn* https://python-graph-gallery.com/25-histogram-with-several-variables-seaborn
- *Control color in seaborn heatmaps* https://python-graph-gallery.com/92-control-color-in-seaborn-heatmaps
5. Kashnitsky, Y. (2021) *Topic 1. Exploratory Data Analysis with Pandas.* https://www.kaggle.com/code/kashnitsky/topic-1-exploratory-data-analysis-with-pandas/notebook
6. Pandas (n.d.) *DataFrame.* https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
7. Pandey, P. (2019) *Getting more value from the Pandas’ value_counts()* https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6
8. Ranjan, S. (2020) *Python | Pandas dataframe.corr().* https://www.geeksforgeeks.org/python-pandas-dataframe-corr/
9. Solomon, B. (2018) *Python Histogram Plotting: NumPy, Matplotlib, Pandas & Seaborn.* https://realpython.com/python-histograms/
10. Souveek (2021) *Python statistics | mean() function.* https://www.geeksforgeeks.org/python-statistics-mean-function/
11. StockOverflow (2019 & 2020):
    - *Append a Header for CSV file?* https://stackoverflow.com/questions/28162358/append-a-header-for-csv-file/28162530#28162530
    - *What are the arguments of seaborn's distplot used for?* https://stackoverflow.com/questions/56707800/what-are-the-arguments-of-seaborns-distplot-used-for
12. Stopak, J (2021) *Writing to a File with Python's print() Function* https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
13. The Matplotlib Development Team (n.p.)
    - *matplotlib.pyplot* https://matplotlib.org/stable/api/pyplot_summary.html
    - *Title positioning* https://matplotlib.org/3.5.0/gallery/text_labels_and_annotations/titles_demo.html
14. W3Schools (n.p.):
    - *Matplotlib Plotting.* https://www.w3schools.com/python/matplotlib_plotting.asp
    - *Pandas - Analyzing DataFrames.* https://www.w3schools.com/python/pandas/pandas_analyzing.asp
    - *Seaborn.* https://www.w3schools.com/python/numpy/numpy_random_seaborn.asp#
15. Waskom, M. (n.d) *seaborn.histplot* https://seaborn.pydata.org/generated/seaborn.histplot.html
16. Wikipedia (2022) *Iris flower data set* https://en.wikipedia.org/wiki/Iris_flower_data_set
