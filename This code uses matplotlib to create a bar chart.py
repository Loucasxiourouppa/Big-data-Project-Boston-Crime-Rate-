import pandas as pd
import matplotlib.pyplot as plt

# Load data from file
df = pd.read_csv('boston_crimerate_modified_newest_version.csv')

# Create plot
plt.figure(figsize=(10, 6))
df['OFFENSE_DESCRIPTION'].value_counts().plot(kind='bar', fontsize=5)

# Adds labels and titles for chart to make sense
plt.xlabel('Offense Description', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Crime Distribution in Boston', fontsize=14)

# Shows chart
plt.show()
