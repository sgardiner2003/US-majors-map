import pandas as pd
import os
import sys
import numpy as np
from urllib.request import urlopen
# print(sys.executable)
# using python 3.11.9; should switch to most recent

"""
LESSONS LEARNED!!!
Must be using the same venv as where you installed geopandas, etc.!
Use where python to get path to python folder
In python folder, go to Lib->site-packages to find osgeo (if not there, then it was installed incorrectly?)
Open osgeo folder and copy path, add to environment variables
IF USING VENV IN VSCODE! ctrl+shift+P, Python: Select Interpreter, then select THE SAME VENV that you downloaded packages in
To download the packages, just do pip install and then the path to the wheel downloaded from github in downloads folder
Next time use conda...

Big totals:

S1502_C06_001E : Percent Females!!Estimate!!Total population 25 years and over with a Bachelor's degree or higher
S1502_C06_001M : Percent Females!!Margin of Error!!Total population 25 years and over with a Bachelor's degree or higher
S1502_C04_001E : Percent Males!!Estimate!!Total population 25 years and over with a Bachelor's degree or higher
S1502_C04_001M : Percent Males!!Margin of Error!!Total population 25 years and over with a Bachelor's degree or higher
Don't think that there is percent m/f total pop 25 to 39 with a bachelors deg

Science and engineering

S1502_C04_008E	Percent Males!!Estimate!!DETAILED AGE!!25 to 39 years!!Science and Engineering
S1502_C04_008M	Percent Males!!Margin of Error!!DETAILED AGE!!25 to 39 years!!Science and Engineering
S1502_C06_008E	Percent Females!!Estimate!!DETAILED AGE!!25 to 39 years!!Science and Engineering
S1502_C06_008M	Percent Females!!Margin of Error!!DETAILED AGE!!25 to 39 years!!Science and Engineering

Science and engineering related fields

S1502_C04_009E	Percent Males!!Estimate!!DETAILED AGE!!25 to 39 years!!Science and Engineering Related Fields
S1502_C04_009M	Percent Males!!Margin of Error!!DETAILED AGE!!25 to 39 years!!Science and Engineering Related Fields
S1502_C06_009E	Percent Females!!Estimate!!DETAILED AGE!!25 to 39 years!!Science and Engineering Related Fields
S1502_C06_009M	Percent Females!!Margin of Error!!DETAILED AGE!!25 to 39 years!!Science and Engineering Related Fields

Business

S1502_C04_010E	Percent Males!!Estimate!!DETAILED AGE!!25 to 39 years!!Business
S1502_C04_010M	Percent Males!!Margin of Error!!DETAILED AGE!!25 to 39 years!!Business
S1502_C06_010E	Percent Females!!Estimate!!DETAILED AGE!!25 to 39 years!!Business
S1502_C06_010M	Percent Females!!Margin of Error!!DETAILED AGE!!25 to 39 years!!Business

Education

S1502_C04_011E	Percent Males!!Estimate!!DETAILED AGE!!25 to 39 years!!Education
S1502_C04_011M	Percent Males!!Margin of Error!!DETAILED AGE!!25 to 39 years!!Education
S1502_C06_011E	Percent Females!!Estimate!!DETAILED AGE!!25 to 39 years!!Education
S1502_C06_011M	Percent Females!!Margin of Error!!DETAILED AGE!!25 to 39 years!!Education

Humanities and others

S1502_C04_012E	Percent Males!!Estimate!!DETAILED AGE!!25 to 39 years!!Arts, Humanities and Others
S1502_C04_012M	Percent Males!!Margin of Error!!DETAILED AGE!!25 to 39 years!!Arts, Humanities and Others
S1502_C06_012E	Percent Females!!Estimate!!DETAILED AGE!!25 to 39 years!!Arts, Humanities and Others
S1502_C06_012M	Percent Females!!Margin of Error!!DETAILED AGE!!25 to 39 years!!Arts, Humanities and Others

"""

### Changing working directory
os.chdir('C:/Users/sophi/OneDrive/Documents/US Majors/')

### Load in data sets

years = [2015,2016,2017,2018,2019,2021,2022,2023,2024]
counties = {}
for year in years:
    df = pd.read_csv(f'by county/ACSST1Y{year}.S1502-Data.csv')
    df.replace('N', np.nan, inplace=True) # this replaces the 'N' values with NaN so that isna() and others will work
    # best to do this when the data frame is loaded initially so that every step after is unaffected (root of the problem)
    counties[year] = df.iloc[1:820] # cutting out the PR counties b/c plotly doesn't display them
    # would be better to just download the right data set next time

states = {}
for year in years:
    state_df = pd.read_csv(f'by state/ACSST1Y{year}.S1502-Data.csv')
    state_df.replace('N', np.nan, inplace=True)
    states[year] = state_df.iloc[1:]

bad_counties = set()
for year,df in counties.items():
    for major in ['S1502_C04_008E','S1502_C06_008E','S1502_C04_009E','S1502_C06_009E','S1502_C04_010E','S1502_C06_010E','S1502_C04_011E','S1502_C06_011E','S1502_C04_012E','S1502_C06_012E']:
        bad_counties.update(df[df[major].isna()].index)
# print(1-len(bad_counties) / len(counties[2015]['GEO_ID'])) # 20.9% of counties are not included -- only 79.1% included
# I wonder what percent of population or land area that is?

bad_states = set()
for year,df in states.items():
    for major in ['S1502_C04_008E','S1502_C06_008E','S1502_C04_009E','S1502_C06_009E','S1502_C04_010E','S1502_C06_010E','S1502_C04_011E','S1502_C06_011E','S1502_C04_012E','S1502_C06_012E']:
        bad_states.update(df[df[major].isna()].index)
# no bad states! but are they just extrapolating data for the state using very limited data from counties?

county_data = {year : counties[year].drop(index = bad_counties) for year in years}
state_data = {year : states[year].drop(index = bad_states) for year in years}
# print(states[2015].iloc[1]) # better way to get column names?

### ADDING FIPS CODES COLUMNS

# want to create column with correct fips codes pulled from GEO_ID col in df
# ex: 0500000US47157 want to cut off first 9 chars
fips = {}
for year in years:
    fips[year] = county_data[year]["GEO_ID"]
    fips[year] = fips[year].str.removeprefix("0500000US")

### MAJORS

# Each one is the percent of m/f between ages 25 and 39 with a degree in science and engineering,
# sci eng related fields, business, education, or humanities.

# difference = new_data[2015]['S1502_C04_008E'].astype("float") - new_data[2015]['S1502_C06_008E'].astype("float")
# print(difference) # males - females generally positive

majors = {}
for name,data in {'county' : county_data, 'state' : state_data}.items():
    majors[name] = {}
    for year in years:
        df = data[year]
        majors[name][year] = {
        'se_diff' : df['S1502_C04_008E'].astype("float") - df['S1502_C06_008E'].astype("float"),
        'ser_diff' : df['S1502_C04_009E'].astype("float") - df['S1502_C06_009E'].astype("float"),
        'bus_diff' : df['S1502_C04_010E'].astype("float") - df['S1502_C06_010E'].astype("float"),
        'edu_diff' : df['S1502_C04_011E'].astype("float") - df['S1502_C06_011E'].astype("float"),
        'hum_diff' : df['S1502_C04_012E'].astype("float") - df['S1502_C06_012E'].astype("float")
        }
# what is counted in ser? what's counted in se? does census tell us?

### CONVERTING TO DATA FRAME

county_frames = []
state_frames = []

for year in years:
    ctdf = pd.DataFrame({
        'year': year,
        'fips': fips[year].values,
        **majors['county'][year]
        }
    )
    stdf = pd.DataFrame({
        'year' : year,
        'state' : state_data[year]["NAME"],
        **majors['state'][year]
    })
    county_frames.append(ctdf)
    state_frames.append(stdf)

final_counties = pd.concat(county_frames, ignore_index=True) # ignore_index=True very important for avoiding index like 0 1 0 1 instead of 0 1 2 3
final_states = pd.concat(state_frames, ignore_index=True)

final_counties.to_csv('C:/Users/sophi/Downloads/counties.csv',index=False)
final_states.to_csv('C:/Users/sophi/Downloads/states.csv',index=False)