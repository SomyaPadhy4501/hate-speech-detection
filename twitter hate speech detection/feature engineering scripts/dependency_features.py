import json
import pandas as pd

# Update the path to the CSV file
csv_file_path = 'C:\\Users\\aryan\\OneDrive\\Desktop\\project\\hate-speech-detection\\feature engineering scripts\\dependency_dict.json'

# Load the file
dependency_dict = json.loads(open(csv_file_path).read())
data = pd.read_csv('cleaned_tweets.csv', encoding='ISO-8859-1')

#find all dependency types found in our dataset, stored in set to ensure no repeats (all unique types)
dependency_types = set()
for key, values in dependency_dict.items():
    for v in list(values):
        dependency_types.add(list(v)[0])

#initialize columns (of all zeros) in dataframe for each of the dependency types
for dependency_type in dependency_types:
    data[str(dependency_type)] = 0

for index, row in data.iterrows():
    tweet = str(row['tweet'])
    clean_tweet = str(row['clean_tweet'])
    idx = str(row['index'])
    dependency_vec = dependency_dict[idx]
    #for each dependency type that tweet contains, add one to that dependency column
    for dependency in dependency_vec:
        data.loc[index, str(dependency[0])] += 1

data = data.add_prefix('dependency:')
data.to_csv("dependency_features.csv", index=False)
