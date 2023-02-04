--#1 query: album title and release year		
SELECT album_title, release_year FROM album WHERE release_year = 2018;

--#2 query: title and duration of the longest track
SELECT track_title, duration_in_sec FROM track WHERE duration_in_sec = (SELECT max(duration_in_sec) FROM track);

--#3 query: track title with duration >= 3.5 min
SELECT track_title FROM track WHERE duration_in_sec >= 3.5*60;

--#4 query: collections title with release 2018 - 2020 years
SELECT collection_title FROM collection WHERE realese_year BETWEEN 2018 AND 2020;

-- #5 query: one word artist name
SELECT artist_name FROM artist WHERE artist_name NOT LIKE '% %';

--#6 query: 'мой/my'
SELECT track_title FROM track WHERE track_title LIKE '%my%' OR track_title LIKE '%мой%';