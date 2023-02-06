--#1 количество исполнителей в каждом жанре
SELECT genre_name, count(genre_name) amount_artists FROM genre g
JOIN artist_genre ag ON g.genre_id = ag.genre_id
GROUP BY genre_name ORDER BY amount_artists DESC;

--#2 количество треков, вошедших в альбомы 2019-2020 годов
SELECT count(track_title) amount_tracks FROM track t
WHERE album_id IN (SELECT album_id FROM album WHERE release_year BETWEEN 2019 AND 2020);

--#3 средняя продолжительность треков по каждому альбому
SELECT album_id, avg(duration_in_sec) mean_duration FROM track
GROUP BY album_id ORDER BY mean_duration DESC;

--#4 все исполнители, которые не выпустили альбомы в 2020 году
SELECT artist_name FROM artist
WHERE artist_id NOT IN (SELECT artist_id FROM artist_album aa
JOIN album a ON aa.album_id = a.album_id WHERE a.release_year = 2020); 

-- #5 названия сборников, в которых присутствует конкретный исполнитель Drake
SELECT DISTINCT (collection_title) FROM collection c
JOIN track_collection tc  ON c.collection_id = tc.collection_id
JOIN track t ON tc.track_id = t.track_id
JOIN album a ON a.album_id = t.album_id
JOIN artist_album aa ON aa.album_id = a.album_id 
JOIN artist a2 ON aa.artist_id = a2.artist_id WHERE a2.artist_name = 'Drake'
ORDER BY collection_title;

--#6 название альбомов, в которых присутствуют исполнители более 1 жанра
SELECT album_title FROM album a
JOIN artist_album aa ON a.album_id = aa.album_id 
JOIN artist_genre ag ON aa.artist_id = ag.artist_id
GROUP BY album_title
HAVING count(album_title) > 1;

--#7 наименование треков, которые не входят в сборники
SELECT track_title FROM track t
WHERE track_id NOT IN (SELECT track_id FROM track_collection);

--#8 исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)
SELECT artist_name FROM artist a 
JOIN artist_album aa ON a.artist_id = aa.artist_id 
JOIN track t ON aa.album_id = t.album_id
WHERE t.duration_in_sec IN (SELECT min(duration_in_sec) FROM track); 

--#9 название альбомов, содержащих наименьшее количество треков
SELECT album_title FROM album a
JOIN track t ON a.album_id = t.album_id
GROUP BY album_title
HAVING count(album_title) = (SELECT count(album_id) FROM track
													GROUP BY album_id 
													ORDER BY count(album_id) LIMIT 1);