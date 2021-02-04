#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: './data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('./data/iris.csv')
classes = df['class'].unique()
print(df.head())

# Define the traces

# HINT:
# This grabs the petal_length column for a particular flower
flower_classes = [flower_class for flower_class in df['class'].unique()]
data = [df[df['class']==flower_class]['petal_length'] for flower_class in flower_classes]


fig = ff.create_distplot(data, flower_classes)
pyo.plot(fig, filename='ex7_distplot.html')
