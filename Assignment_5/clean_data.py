import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
condition = (cleaned_df['age'] > 17) & (cleaned_df['year'] < 2025)
cleaned_df = cleaned_df[condition]
for x in selected:
    mean = cleaned_df[x].mean()
    sd = cleaned_df[x].std()
    print(mean,sd)
    plt.figure(figsize=(10, 6))
    sns.histplot(cleaned_df[x], bins=100, kde=True, color='skyblue', stat="density")
    # Plotting the mean and standard deviation lines
    plt.axvline(mean, color='r', linestyle='--', label=f'Mean: {mean:.2f}')
    plt.axvline(mean + sd, color='g', linestyle='--', label=f'+1 SD: {mean + sd:.2f}')
    plt.axvline(mean - sd, color='g', linestyle='--', label=f'-1 SD: {mean - sd:.2f}')
    plt.title(f'{x} with Mean and Standard Deviation')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()
    plt.show()
parser = argparse.ArgumentParser(description='Export DataFrame to CSV file.')
parser.add_argument('filename', type=str, default="cleaned_population_data.csv")
# Parse the command-line arguments
args = parser.parse_args()
# Export the DataFrame to CSV using the provided filename
cleaned_df.to_csv(args.filename, index=False)
print(f'DataFrame exported to {args.filename}')

