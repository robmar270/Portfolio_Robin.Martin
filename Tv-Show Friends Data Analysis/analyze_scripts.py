import os
import pandas as pd
import re

# Path to CSV files
folder_path = ''

# list to store the data
data = []

# patterns to extract season, episode, title, and character
episode_pattern = r"s(\d{2})E(\d{2})(?:-S\d{2}E\d{2})?\s+(.+)"  # Pattern for "s03E25 At The Beach" or "S10E17-S10E18 The Last One Part I II"
character_line_pattern = r"([A-Za-z ]+):\s*(.*)"  # Pattern to match "Character: Line" format

# Loop through all files in the CSV files
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):  
        # Use regex to extract season, episode, and title
        match = re.match(episode_pattern, filename, re.IGNORECASE)
        if match:
            season_number = int(match.group(1))  # Season number
            episode_number = int(match.group(2))  # Episode number
            episode_title = match.group(3).strip()  # Episode title

            # Open and read the content of the episode file
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # Loop through each line and append data
            for line in lines:
                # Clean up any unwanted characters
                line = line.strip()
                if line:  # Only process non-empty lines
                    char_match = re.match(character_line_pattern, line)
                    if char_match:
                        character = char_match.group(1).strip()  # Character name
                        dialogue = char_match.group(2).strip()  # Dialogue

                        # Append to the data list
                        data.append({
                            "Season": season_number,
                            "Episode": episode_number,
                            "Title": episode_title,
                            "Character": character,
                            "Line": dialogue
                        })

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
output_csv_path = ''
df.to_csv(output_csv_path, index=False)

print(f"Data has been saved to {output_csv_path}")
