#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('./data/mpg.csv')

# create data by choosing fields for x, y and marker size attributes
print(df.head())

data = [go.Scatter(
    x=df['horsepower']
    , y=df['weight']
    , text=df['name']
    , mode='markers'
    , marker=dict(size=1.5*df['mpg']
                  , showscale=True
                  , color = df['cylinders']
                  )
)]

# create a layout with a title and axis labels
layout = go.Layout(
    title=''
    , xaxis = dict(title='horsepower')
    , yaxis = dict(title='weight')
    , hovermode='closest'
    
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='ex4_bubble_chart.html')