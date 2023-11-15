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

# Full
f = open('processed/all.csv', 'w')
f.write('text\n')
f.writelines(data)
f.close()

# Train
f = open('processed/train.csv', 'w')
f.write('text\n')
f.writelines(train)
f.close()

# Test
f = open('processed/test.csv', 'w')
f.write('text\n')
f.writelines(test)
f.close()

