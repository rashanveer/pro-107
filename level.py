import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("data.csv")

levelData = df.groupby("level")["attempt"].mean()

as_index = False

print(levelData)

fig = px.scatter(df,x = levelData,y = ['Level 1','Level 2','level 3','level 4'])

fig.show()