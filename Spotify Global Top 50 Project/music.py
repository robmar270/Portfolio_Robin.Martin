import os
import pandas as pd
from sqlalchemy import create_engine, BigInteger, String, Date
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

def setup_spotify_client():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    return Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def fetch_playlist_data(sp, playlist_id):
    try:
        results = sp.playlist_tracks(playlist_id)
        return results['items']
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

def transform_data(results):
    songs_data = []
    fetch_date = datetime.now().strftime('%Y-%m-%d')  
    for idx, item in enumerate(results, start=1):
        track = item['track']
        song_info = {
            'playlist_order': idx,
            'track_name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'release_date': track['album']['release_date'],  
            'popularity': track['popularity'],
            'fetch_date': fetch_date  # Add today's date as fetch date
        }
        songs_data.append(song_info)

    # Convert to DataFrame
    df = pd.DataFrame(songs_data)
    
    # Convert data types explicitly
    df['playlist_order'] = df['playlist_order'].astype('int64')
    df['popularity'] = df['popularity'].astype('int64')
    df['rank'] = df['popularity'].rank(method='max', ascending=False).astype(int)
    
    # Convert release_date and fetch_date to datetime
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce').dt.date  # Convert to date type
    df['fetch_date'] = pd.to_datetime(df['fetch_date']).dt.date  # Convert to date type

    return df.sort_values(by='playlist_order')

def load_to_db(df):
    db_url = os.getenv("DATABASE_URL")
    engine = create_engine(db_url)

    # Ensure correct data types in the SQL table using SQLAlchemy types
    df.to_sql('spotify_top_tracks', engine, if_exists='replace', index=False, 
              dtype={
                  'playlist_order': BigInteger(),
                  'popularity': BigInteger(),
                  'rank': BigInteger(),
                  'album': String(),
                  'release_date': Date(),
                  'fetch_date': Date(),
                  'track_name': String(),
                  'artist': String()
              })
    
    print("Data has been successfully loaded to the database.")

# Main Execution
if __name__ == "__main__":
    playlist_id = '37i9dQZEVXbMDoHDwVN2tF'
    
    sp = setup_spotify_client()
    playlist_data = fetch_playlist_data(sp, playlist_id)
    if playlist_data:
        df = transform_data(playlist_data)
        load_to_db(df)
