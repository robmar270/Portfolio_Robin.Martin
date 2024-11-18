import pandas as pd

# Load the CSV files with error handling
try:
    friends_episodes = pd.read_csv('')
    friends_imdb = pd.read_csv('', encoding='ISO-8859-1', on_bad_lines='skip')
    print("Files loaded successfully.")
except Exception as e:
    print(f"Error loading files: {e}")

# Data Quality Checks
# 1. Missing Values Check
print("Missing Values Check:")
missing_summary = friends_episodes.isnull().sum()
print(missing_summary[missing_summary > 0])  # Only shows columns with missing values

missing_summary_imdb = friends_imdb.isnull().sum()
print(missing_summary_imdb[missing_summary_imdb > 0])  # Missing values in friends_imdb

# 2. Duplicate Rows Check
print("\nDuplicate Rows Check:")
duplicate_rows_episodes = friends_episodes[friends_episodes.duplicated()]
if duplicate_rows_episodes.empty:
    print("No duplicate rows found in friends_episodes.")
else:
    print(f"{len(duplicate_rows_episodes)} duplicate rows found in friends_episodes. Removing duplicates.")
    friends_episodes = friends_episodes.drop_duplicates()

duplicate_rows_imdb = friends_imdb[friends_imdb.duplicated()]
if duplicate_rows_imdb.empty:
    print("No duplicate rows found in friends_imdb.")
else:
    print(f"{len(duplicate_rows_imdb)} duplicate rows found in friends_imdb. Removing duplicates.")
    friends_imdb = friends_imdb.drop_duplicates()

# Drop the 'episode_num_overall' column from friends_episodes before merging
friends_episodes = friends_episodes.drop(columns=['episode_num_overall'])

# Merge the two DataFrames based on the season, episode number in season, and title columns
merged_df = pd.merge(friends_episodes, friends_imdb, left_on=['season', 'episode_num_in_season', 'title'], 
                     right_on=['season', 'episode_num', 'title'], how='left')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('', index=False)

print("Data has been merged and saved to 'merge_friends_data.csv'.")
