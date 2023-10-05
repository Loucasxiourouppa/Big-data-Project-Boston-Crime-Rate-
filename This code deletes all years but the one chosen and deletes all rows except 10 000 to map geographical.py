import pandas as pd

# Reads the CSV file
df = pd.read_csv('boston_crimerate_modified_newest_version.csv')

# Keeps only rows where the year is 2018
df = df[df['YEAR'] == 2018]

# Keeps random 10,000 rows 
df = df.head(10000)

# Saves  modified CSV file
df.to_csv('boston_crimerate_modified_2018.csv', index=False)
