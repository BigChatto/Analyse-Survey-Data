import pandas as pd

# Read the data into a DataFrame
df = pd.read_csv('survey_data.csv')

# Calculate the average of a specific column
average_response = df['Question1'].mean()
