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
