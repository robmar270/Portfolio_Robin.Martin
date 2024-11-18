# 📊 Data Analysis Project: The TV Show *Friends*

## Introduction  
The TV show *Friends* is a legendary sitcom loved by millions worldwide. I wanted to explore why it has remained so appealing and uncover interesting insights from the data. Using two datasets from Kaggle—one with structured episode data and another with the complete script—I aimed to answer the following key questions:

1. How has the total number of lines for each character evolved across the series?  
2. Can we dive deeper into insights at the season and episode level?  
3. Which writers and producers were most involved in creating *Friends*?  
4. What were the least and most viewed/rated episodes or seasons?  
5. How many times did Joey say his iconic line, *“How you doin’?”*  

By combining data manipulation, cleaning, and visualization, I built a comprehensive dashboard in Tableau to uncover these insights.

---

## Data Sources  
- **Friends Dataset ([Kaggle](https://www.kaggle.com/datasets/bcruise/friends-episode-data/data?select=friends_episodes.csv))**: Contains details like season, episode, title, air date, IMDb ratings, and US viewership.  
- **Friends Script Dataset ([Kaggle]https://www.kaggle.com/datasets/blessondensil294/friends-tv-series-screenplay-script)**: Includes every line spoken in the show, tagged with the character and episode details.  

---

## Tools & Technologies  
- **Python**: For data cleaning and preparation using Pandas.  
- **Google Sheets**: For manual corrections and initial exploration.  
- **Tableau**: To create an interactive dashboard for analysis and visualization.  

---

## Process  

### Step 1: Data Exploration and Cleaning  
- Explored the datasets in Google Sheets to understand their structure.  
- Found and resolved issues, such as combined rows for multiple episodes.  
- Used Python and Pandas to:  
  - Split combined episodes into separate rows.  
  - Standardized character names (e.g., converting *"Rach"* to *"Rachel"*).  
  - Fixed shared lines by splitting them for each character (e.g., *"Monica and Chandler"*).  
  - Verified and corrected non-standard character names like *"Dream Monica"* and *"Gunther"*.  

### Step 2: Data Preparation for Tableau  
- Joined the datasets dynamically in Tableau using season and episode numbers.  
- Optimized datasets by removing unnecessary columns (e.g., summaries and descriptions).  
- Converted key columns (e.g., `original_air_date`) to a datetime format for time-based analysis.  

### Step 3: Dashboard Design  
- Brainstormed and implemented visualizations to answer the key questions effectively.  
- Added interactive filters for season, episode, character, writers, and producers.  
- Styled the dashboard to be user-friendly and visually appealing.  

---

## Findings  

### Key Insights from the Dashboard  
- **Character Line Evolution**: Rachel consistently had the most lines across the series, while Joey saw a significant increase in later seasons.  
- **Seasonal and Episode-Specific Analysis**:  
  - Highest-rated episode: *The One Everybody Finds Out* & *The Last One* (IMDb 9.7).  
  - Lowest-rated episode: *The One with the Invitation* (IMDb 7.1).  
  - Most-viewed episode: *The One After the Superbowl* (52.9M viewers).  
  - Least-viewed episode: *The One with the Vows* (15.6M viewers).  

- **Top Writers and Producers**:  
  - Gary Halvorson directed the most episodes.  
  - Andrew Reich & Ted Cohen wrote the most episodes.  

- **Joey’s Iconic Line**:  
  - *“How you doin’?”* was said **25 times** by Joey.  
  - Other characters also said it: Ross (4), Rachel (4), Monica (2).  

- **Viewer Trends**:  
  - Average US viewers ranged from **20 to 30 million**.  

---

## Interactive Dashboard  
The Tableau dashboard enables users to:  
- Filter by season, episode, character, writer, and producer.  
- View character-specific insights and evolution over the series.  
- Compare IMDb ratings and US viewership for all episodes.  
- Identify the most and least popular episodes quickly.  

👉 **[View the Tableau Public Dashboard](https://public.tableau.com/app/profile/robin.martin1864/viz/TheOnewithAlltheData/Friends)**  

---

## Future Improvements  
- Perform sentiment analysis on the script to determine emotional trends across seasons.  
- Explore correlations between episode ratings and specific characters or writers.  
- Add more granular insights into supporting characters’ lines and patterns.  

---

## Conclusion  
This project highlights how combining scripting tools like Python and visualization tools like Tableau can create powerful insights from raw data. The analysis of *Friends* offers a glimpse into what made this show a cultural phenomenon and provides opportunities for deeper exploration.
