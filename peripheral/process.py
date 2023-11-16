import glob
import csv
import pandas as pd
from sklearn.model_selection import train_test_split

# Read text files from a directory using glob
file_list = glob.glob('raw/*.txt')  # Replace 'path/to/your/text/files/' with your directory path
data = []

for file_path in file_list:
    with open(file_path, 'r') as file:
        content = file.readlines()
        data.extend(content)

# Split the shuffled data into 70% training and 30% testing using sklearn
train, test = train_test_split(data, test_size=0.3, random_state=42)

# Make dataframes
full_df = pd.DataFrame(data, columns=['text'])
train_df = pd.DataFrame(train, columns=['text'])
test_df = pd.DataFrame(test, columns=['text'])

# Remove newlines
full_df['text'] = full_df['text'].str.replace('\n','')
train_df['text'] = train_df['text'].str.replace('\n','')
test_df['text'] = test_df['text'].str.replace('\n','')

# Write out
full_df.to_csv('processed/all.csv', sep='\t', index=False, quoting=csv.QUOTE_ALL)
train_df.to_csv('processed/train.csv', sep='\t', index=False, quoting=csv.QUOTE_ALL)
test_df.to_csv('processed/test.csv', sep='\t', index=False, quoting=csv.QUOTE_ALL)