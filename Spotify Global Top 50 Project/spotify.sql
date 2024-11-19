/* Check data types if it has inserted in correctly */ 
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'spotify_top_tracks';

/* Show artist that has more than 1 song on playlist */
SELECT artist, COUNT(track_name) AS song_count
FROM spotify_top_tracks
GROUP BY artist
HAVING COUNT(track_name) >= 2
ORDER BY song_count DESC;

/* Show artists that the highest rank in popularity in order */
SELECT *
FROM spotify_top_tracks
ORDER BY popularity DESC;

/* Newest song */
SELECT artist, track_name, release_date
FROM spotify_top_tracks
ORDER BY release_date DESC
LIMIT 1;  -- Newest song

/* Oldest song */
SELECT artist, track_name, release_date
FROM spotify_top_tracks
ORDER BY release_date ASC
LIMIT 1; 

/* When does popularity ranking compare to the most streamed song falling into the same list number */
WITH ranked_tracks AS (
    SELECT track_name, popularity, RANK() OVER (ORDER BY popularity DESC) AS popularity_rank
    FROM spotify_top_tracks
)
SELECT t1.track_name, t1.popularity_rank
FROM ranked_tracks t1
JOIN ranked_tracks t2 ON t1.popularity_rank = t2.popularity_rank
WHERE t2.track_name = (SELECT track_name FROM ranked_tracks ORDER BY popularity DESC LIMIT 1);

/* What is the most common used word */
SELECT word, COUNT(*) AS word_count
FROM (
    SELECT unnest(string_to_array(lower(track_name), ' ')) AS word
    FROM spotify_top_tracks
) AS words
GROUP BY word
ORDER BY word_count DESC
LIMIT 1;

/* Count of the year each song was released*/
SELECT 
    TO_CHAR(release_date, 'YYYY') AS release_year,  -- Format release_date to 'YYYY'
    COUNT(track_name) AS song_count
FROM 
    spotify_top_tracks
GROUP BY 
    TO_CHAR(release_date, 'YYYY')
ORDER BY 
    release_year DESC;


