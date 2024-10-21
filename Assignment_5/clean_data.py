import pandas as pd
import argparse
#loading in the dataset
data = pd.read_csv('messy_population_data.csv', delimiter=',')
dataset = pd.DataFrame(data)
#selected columns for analysis
selected = ['age', 'gender', 'year', 'population']
#Issue 1 : dropping the rows that have na values
cleaned_df = dataset.dropna()
#Issue 2 : dropping the rows that have na values
cleaned_df = cleaned_df.drop_duplicates()
#issue 3: some data rows don't make sense
condition = (cleaned_df['age'] > 17) & (cleaned_df['year'] < 2025) & (cleaned_df['population'] < 10000000)
cleaned_df = cleaned_df[condition]
#export
parser = argparse.ArgumentParser(description='Export DataFrame to CSV file.')
parser.add_argument('filename', type=str, default="cleaned_population_data.csv")
# Parse the command-line arguments
args = parser.parse_args()
# Export the DataFrame to CSV using the provided filename
cleaned_df.to_csv(args.filename, index=False)
print(f'DataFrame exported to {args.filename}')

