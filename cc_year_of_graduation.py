# -*- coding: utf-8 -*-
"""CC_year of Graduation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zwMwjBQRBqHrhUbfECtcTQUyZPXIHBPt
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel('/content/Final Lead Data.xlsx')

data.head(5)

data.columns

data.info()

# Checking for Null values
data.isna().sum()

# Checking for duplicate values
data[data.duplicated]

data.shape

# We pick two approaches here to find the graduation year,
# 1. When academic year value is specified
# 2. When academic year value is unspecified

# Approach 1: When Academic value is known

# We have values specified in both 'Academic Year' & 'What is your current academic year?' columns

# Merging data from Columns 'Academic Year' and 'What is your current academic year?' into single column

data['Academic Year'] = data['Academic Year'].fillna(data['What is your current academic year?'])

columns_to_drop=["Position","Gender","City","Colleges","New College Name","Branch/ Specialisation","Company Name/ College Name","What is your current academic year?","Would you like to know more about us and our programs?","Are you interested in knowing more about our events?","Have you recommended Cloud Counselage to anyone?","How did you come to know about this event?","Email","Other Branch"]
data.drop (columns_to_drop, axis=1, inplace=True)

data.head(2)

data.isna().sum()

# Now, we Convert the 'Created' column to datetime format
data['Created'] = pd.to_datetime(data['Created'])

# Extracting only the year from the 'Created' column into a separate column called 'Created Year'
data['Created Year'] = data['Created'].dt.year

# Coverting 'Academic year to type:int'
data['Academic Year'] = pd.to_numeric(data['Academic Year'], errors='coerce').astype('Int64')

# Implementing Approach 1
# Calculating the Graduation Year when the Academic year is known
data['Graduation Year'] = data['Created Year'] + data['Academic Year']

data

# Approach 2: To predict the graduation year when Academic Year is unknown

# Since, the duration of most of the engineering degrees are 4 years, We assume that Avg.Duration is 4
# Creating a new column avg duration

data['Avg.Duration'] = 4

data.loc[data['Academic Year'].isna(), 'Graduation Year'] = data['Created Year'] + data['Avg.Duration']

data

data.describe()

#Downloading the graduation year output file
file_path = "/content/graduation_year_output_file.xlsx"

data.to_excel(file_path, index=False)

# Heat map for Correlation of variables

sns.set(style="white")
plt.rcParams['figure.figsize'] = (10, 5)
corrmat=sns.heatmap(data.corr(), annot = True, linewidths=.1, cmap="Blues")
plt.title('Corelation Between Variables', fontsize = 10)
plt.show()