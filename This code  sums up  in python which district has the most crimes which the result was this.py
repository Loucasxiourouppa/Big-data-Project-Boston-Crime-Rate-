import pandas as pd

# load data 
df = pd.read_csv('boston_crimerate_modified_newest_version.csv')

# uses value_counts to count number of crimes in each district
district_counts = df['DISTRICT'].value_counts()

# displays the result
print(district_counts)
