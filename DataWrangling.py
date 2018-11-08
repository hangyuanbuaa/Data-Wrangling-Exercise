# Data Wrangling: Gathering > Assessing > Cleaning (Jupyter Notebook)
#----------------------------------------------------
# Step 1: Gather
import pandas as pd
import zipfile

with zipfile.ZipFile('file.zip', mode='r') as myzip:
#    myzip.write('xxx.txt')
    myzip.extractall()

df = pd.read_csv('file.csv')
#----------------------------------------------------
# Step 2: Assess
# a. Visual assessment
df
# b. Programmatic assessment
df.info()
df.head()
df.tail()
df['col1'].value_counts()

# Write down the issues of dirty/messy data
# Dirty: low quality content
#        1> missing data; 2> invalid data;
#        3> inaccurate data; 4> inconsistent data
# Messy: structural issues
#----------------------------------------------------
# Step 3: Clean
# Define: convert our assessments into defined cleaning tasks
#         with third level headers (###)denoting issues
#         1> Missing values (NaN)
#         2> Data inconsistencies
#         3> Nondescriptive column heads ...

# Code: convert those definitions to code and run that code
# back up first
df_clean = df.copy()
# rename columns
df_clean = df_clean.rename(columns={'oldName1': 'newName1',
                                    'oldName2': 'newName2'})
# data inconsistencies: replace inconsistent value with one
for phrase in asap_list:
#    df.ix[selection criteria, columns I want] = value
    df_clean.ix[df_clean.StartDate == phrase, 'StateDate'] = 'ASAP'
## Or
    df_clean.StartDate.replace(phrase, 'ASAP', inplace=True)

# Test: check if the cleaning operations worked
df_clean.StartDate.value_counts()
## or use Assert Statements
for phrase in asap_list:
# assert Expression[, Arguments]
# series.values
    assert phrase not in df_clean.StartDate.values
# More steps: Reassess and Iterate, Store

#----------------------------------------------------

# Text Files in Python
import glob
for review in glob.glob('review/*.txt'):
    with open(review, encoding='utf-8') as file:
        file.readline()
        file.read()
#        print(file.readline())
#        break
# in Python 3 always open files with explicit encoding

#----------------------------------------------------

# API > MediaWiki
import wptools

page = wptools.page('E.T._the_Extra-Terrestrial').get()
page.data['image'][0]               # JSON array  > python dict
page.data['infobox']['director']    # JSON object > python list

# or use json library to parse
import simplejson as json

# writing JSON to a file
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

# reading JSON from a file
with open('data.txt') as json_file:
    data = json.loads(json_file)
#----------------------------------------------------

# Relational Databases in python

from sqlalchemy import create_engine
# connect to a database
engine = create_engine('sqlite:///bestofrt.db')
# store pandas DataFrame in Database
df.to_sql('master', engine, index=False)

# read database data into a pandas DataFrame
df_gather = pd.read_sql('SELECT * FROM master', engine)
