import pandas as pd

# Loads the file 
df = pd.read_csv("boston_crimerate.csv")

# Drops columns UCR_PART and OFFENSE_CODE_GROUP
df = df.drop(columns=["UCR_PART", "OFFENSE_CODE_GROUP"])

# Saves the file with new changes
df.to_csv("boston_crimerate_modified.csv", index=False)
