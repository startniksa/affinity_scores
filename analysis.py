# The Jupyter Notebook is accessible at:
# https://colab.research.google.com/drive/1FT6Guam-OnBEjOeWiRpd_WWsFTa9_s_t?usp=sharing
import pandas as pd

# Load the CSV file
data = pd.read_csv('bq-results-20231220-134345-1703079855754.csv')

# Convert 'date' column to datetime and filter for engagements in 2023
data['date'] = pd.to_datetime(data['date'])
data_2023 = data[data['date'].dt.year == 2023]

# Expand the 'topic' column so each topic has its own row
data_2023['topic'] = data_2023['topic'].str.split(';')
data_2023_exploded = data_2023.explode('topic')

# Assign an engagement value of 1 for each row to represent an engagement event
data_2023_exploded['engagement_value'] = 1

# Aggregate engagements per user-topic to get actual counts
actual_engagements = data_2023_exploded.groupby(['scv_id', 'topic']).size().reset_index(name='engagement_count')

# Calculate the maximum number of engagements for each user across all topics
actual_engagements['max_user_engagement'] = actual_engagements.groupby('scv_id')['engagement_count'].transform('max')

# Calculate the affinity score for each user-topic combination relative to the user's maximum engagement
actual_engagements['affinity_score'] = (actual_engagements['engagement_count'] / actual_engagements['max_user_engagement']) * 10

# Save the result to a CSV file for further use
output_file_path = 'user_topic_affinity_scores.csv'
actual_engagements.to_csv(output_file_path, index=False)