import pandas as pd
import matplotlib.pyplot as plt

# Load data from Excel file
df = pd.read_csv('boston_crimerate_modified_newest_version.csv')

# Filter data for 2020 only
df = df[df['YEAR'] == 2020]

# Get the top 20 crime types
top_crimes = df['OFFENSE_DESCRIPTION'].value_counts().head(20)

# Create a bar chart of the top 20 crime types
plt.figure(figsize=(10,8))
plt.bar(top_crimes.index, top_crimes.values)
plt.xticks(rotation=90)
plt.xlabel('Crime Type')
plt.ylabel('Number of Crimes')
plt.title('Top 20 Crime Types in Boston (2020)')
plt.show()
