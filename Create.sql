-- Create tables
CREATE TABLE IF NOT EXISTS genre (
		genre_id SERIAL PRIMARY KEY,
		genre_name VARCHAR(50) UNIQUE);
	
CREATE TABLE IF NOT EXISTS artist (
		artist_id SERIAL PRIMARY KEY,
		artist_name VARCHAR(60) UNIQUE);

CREATE TABLE IF NOT EXISTS album (
		album_id SERIAL PRIMARY KEY,
		album_title VARCHAR(60) NOT NULL,
		release_year INT NOT NULL);

CREATE TABLE IF NOT EXISTS track (
		track_id SERIAL PRIMARY KEY,
		track_title VARCHAR(60) NOT NULL,
		duration_in_sec INT NOT NULL,
		album_id INT REFERENCES album(album_id));

CREATE TABLE IF NOT EXISTS collection (
		collection_id SERIAL PRIMARY KEY,
		collection_title VARCHAR(60) NOT NULL,
		realese_year INT NOT NULL);

CREATE TABLE IF NOT EXISTS artist_genre (
		id SERIAL PRIMARY KEY,
		artist_id INT REFERENCES artist(artist_id),
		genre_id INT REFERENCES genre(genre_id));

CREATE TABLE IF NOT EXISTS artist_album (
		id SERIAL PRIMARY KEY,
		artist_id INT REFERENCES artist(artist_id),
		album_id INT REFERENCES album(album_id));
	
CREATE TABLE IF NOT EXISTS track_collection (
		id SERIAL PRIMARY KEY,
		track_id INT REFERENCES track(track_id),
		collection_id INT REFERENCES collection(collection_id));