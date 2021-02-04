#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
from plotly.graph_objs.graph_objs import Layout
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# create a DataFrame from the .csv file:
df = pd.read_csv('./data/abalone.csv')

# take two random samples of different sizes:
rand_sample_50 = np.random.choice(df['rings'], 50, replace=False)
rand_sample_100 = np.random.choice(df['rings'], 100, replace=False)

# create a data variable with two Box plots:

data = [
    go.Box(
        y=rand_sample_50
        , name='sample 50'
    ),
    go.Box(
        y=rand_sample_100
        , name='sample 100'
    )
]

# add a layout
layout = go.Layout(title='sample 50 vs. sample 100 for Abalone ring size')

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='ex5_box.html')