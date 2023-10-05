import pandas as pd

# load data 
df = pd.read_csv('boston_crimerate_modified_newest_version.csv')

# use the value_counts method to count the number of occurrences of each offence 
offense_counts = df['OFFENSE_DESCRIPTION'].value_counts()

# display the result
print(offense_counts)
