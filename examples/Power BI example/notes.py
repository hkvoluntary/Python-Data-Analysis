
## Power BI with Python demo 
### Get the data from sqlite DB

import sqlite3
import pandas as pd

with sqlite3.connect(r"C:\Users\Administrator\Desktop\Ted\python\powerbi_python\people_database.db") as connection:
    df = pd.read_sql_query("SELECT * FROM people", connection)

########################################


# Data manipulation

# 'dataset' holds the input data for this script
import pandas as pd

dataset[
    ["first_name", "last_name"]
] = dataset["Name"].str.split(n=1, expand=True)
dataset.drop(columns=["Name"], inplace=True)

# Convert to non-numeric values become NaN
dataset['Pets'] = pd.to_numeric(dataset['Pets'], errors='coerce')
# Replace NaN values with 0
dataset['Pets'] = dataset['Pets'].fillna(0)

########################################


# Scatter chart 
# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Age, Weight)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt

# Create a scatter plot
dataset.plot(kind='scatter', x='Age', y='Weight', color='red')
plt.show()

########################################


# Line chart

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(first_name, Children, Pets)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

import matplotlib.pyplot as plt 

# Create a line plot with multiple columns
ax = plt.gca() 
dataset.plot(kind='line',x='first_name',y='Children',ax=ax) 
dataset.plot(kind='line',x='first_name',y='Pets', color='red', ax=ax) 
plt.show()

########################################


# Bar Plot

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Car Color)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

import matplotlib.pyplot as plt 

# Create a bar plot
series = dataset[dataset["Car Color"] != ""].groupby("Car Color").size()
series.plot(kind="bar", color=series.index, edgecolor="black")

plt.show()


