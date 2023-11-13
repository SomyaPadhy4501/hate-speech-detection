import pandas as pd
import re
import string

# Update the path to the CSV file
csv_file_path = 'C:/Users/aryan/OneDrive/Desktop/project/hate-speech-detection/initial datasets/labeled_data.csv'

# Read the CSV file
data = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

clean_tweets = []
for index, row in data.iterrows():
    tweet = str(row['tweet']).lower()
    clean_tweets.append(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()))

# Add cleaned tweets to the DataFrame
data['clean_tweet'] = clean_tweets

# Save cleaned data to a new CSV file
cleaned_csv_file_path = 'C:/Users/aryan/OneDrive/Desktop/project/cleaned_tweets.csv'
data.to_csv(cleaned_csv_file_path, index=False)
