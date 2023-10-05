import pandas as pd

# loads the dataset
df = pd.read_csv('boston_crimerate_modified_newest_version.csv')

# use the value_counts method to sum every crime number in every street.
street_counts = df['STREET'].value_counts()

# displays the result
print(street_counts)

