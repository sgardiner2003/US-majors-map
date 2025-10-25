import pandas as pd
import os
import plotly.express as px
import json
from urllib.request import urlopen

### LOAD DATASETS

os.chdir('C:/Users/sophi/OneDrive/Documents/US Majors/')
counties = pd.read_csv('counties.csv')
states = pd.read_csv('states.csv')

### LINE GRAPHS

state_graph = px.line(states, x='year', y='se_diff',color = 'state')
# make column for region and color code by that to see if trends are different by region (eg northeast)

state_graph.show()