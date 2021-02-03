#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('./data/2010YumaAZ.csv')

# What should go inside this Scatter call?
# data = [{
#     'x': df['LST_TIME']
#     , 'y': df[df['DAY']==day]['T_HR_AVG']
#     , 'name': day
# } for day in df['DAY'].unique()
# ]

data = [go.Scatter(
    x=df['LST_TIME']
    , y=df[df['DAY']==day]['T_HR_AVG']
    , name=day
) for day in df['DAY'].unique()]

# Define the layout
layout = go.Layout(
    title='Average temperature, Yuma, AZ'
)

# Create a fig from data and layout, and plot the fig

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='ex2_linechart.html')
