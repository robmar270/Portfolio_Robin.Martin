# 🎵 Spotify Playlist Analyzer

## 📄 Overview
This project fetches, processes, and analyzes data from a Spotify playlist using Python and SQL. It extracts track details, ranks songs by popularity, and stores the data in a SQL database for advanced querying and insights.

---

## 🚀 Features
- **Data Retrieval**: Fetch tracks and their metadata (artist, album, release date, popularity) from a Spotify playlist.
- **Data Transformation**:
  - Rank tracks by popularity.
  - Clean and structure data into a pandas DataFrame.
  - Convert and standardize data types for seamless database storage.
- **Database Integration**: Save the processed data into a PostgreSQL database with properly defined types.
- **SQL Queries**: Run insightful queries like:
  - Most popular songs.
  - Artists with multiple tracks in the playlist.
  - Oldest and newest songs.
  - Most common words in song titles.

---

## 🛠️ Technologies Used
- **Python**: Data extraction and transformation.
- **Spotify API**: Fetch playlist data.
- **SQLAlchemy**: Database connection and data insertion.
- **PostgreSQL**: Data storage and analysis.
- **Pandas**: Data manipulation.
- **Spotipy**: Simplified interaction with the Spotify API.
- **dotenv**: Manage sensitive credentials.


