"""
Objective: Using the iris dataset, develop a Distplot
that compares the petal lengths of each class.
"""
# Perform imports here:
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

# Create a pandas DataFrame from mpg.csv
df = pd.read_csv('../data/iris.csv')

# Define the traces
trace0 = pd.DataFrame(df[df['class']=='Iris-setosa'])['petal_length']
trace1 = pd.DataFrame(df[df['class']=='Iris-versicolor'])['petal_length']
trace2 = pd.DataFrame(df[df['class']=='Iris-virginica'])['petal_length']

# Define a data variable
hist_data = [trace0, trace1, trace2]
group_labels = ['Iris Setosa','Iris Versicolor','Iris Virginica']

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(hist_data, group_labels)
pyo.plot(fig, filename='solution7.html')

"""
Great! This shows that if given a flower with a petal length
between 1-2cm, it is almost certainly an Iris setosa!
"""