INSERT INTO genre (genre_name) VALUES ('R&B'), ('Hip-hop'), ('Funk-rock'), ('Pop-rock'), ('Alternative'), ('Rap');
INSERT INTO album (album_title, release_year) VALUES ('At._Long._Last._ASAP', 2015), ('Testing', 2018), ('Evolve', 2017),
													('Certified_Lover_Boy', 2021), ('Scorpion', 2018), ('Views', 2016),
													('Origins', 2018), ('DAMN.', 2017), ('Results_May_Vary', 2003),
													('Overexposed', 2012), ('Hollywood’s_Bleeding', 2019), ('The_Getaway', 2016),
													('Californication', 1999);
INSERT INTO artist (artist_name) VALUES ('ASAP Rocky'), ('Drake'), ('Imagine Dragons'), ('Kendrick Lamar'),
										('Limp Bizkit'), ('Maroon 5'), ('Post Malone'), ('Red Hot Chili Peppers');

INSERT INTO track (track_title, duration_in_sec, album_id) VALUES ('Holy Ghost', 191, (SELECT album_id FROM album
																				WHERE album_title='At._Long._Last._ASAP')), ('LSD', 238, (SELECT album_id FROM album 
																				WHERE album_title='At._Long._Last._ASAP')), ('Lord Pretty Flacko Jodye 2 (LPFJ2)', 127, (SELECT album_id FROM album
																				WHERE album_title='At._Long._Last._ASAP')),('Distorted Records', 140, (SELECT album_id FROM album
																				WHERE album_title='Testing')), ('Tony Tone', 208, (SELECT album_id FROM album
																				WHERE album_title='Testing')), ('Buck Shots', 167, (SELECT album_id FROM album
																				WHERE album_title='Testing')), ('Champagne Poetry', 336, (SELECT album_id FROM album
																				WHERE album_title='Certified_Lover_Boy')), ('No Friends In the Industry', 204, (SELECT album_id FROM album
																				WHERE album_title='Certified_Lover_Boy')), ('Survival', 136, (SELECT album_id FROM album
																				WHERE album_title='Scorpion')), ('Sandras Rose', 214, (SELECT album_id FROM album
																				WHERE album_title='Scorpion')), ('Dancing in the Dark', 233, (SELECT album_id FROM album
																				WHERE album_title='Evolve')), ('Believer', 204, (SELECT album_id FROM album
																				WHERE album_title='Evolve')), ('Feel No Ways', 185, (SELECT album_id FROM album
																				WHERE album_title='Views')), ('DNA', 185, (SELECT album_id FROM album
																				WHERE album_title='DAMN.')), ('Loyalty', 227, (SELECT album_id FROM album
																				WHERE album_title='DAMN.')), ('Humble', 177, (SELECT album_id FROM album
																				WHERE album_title='DAMN.')), ('Behind Blue Eyes', 364, (SELECT album_id FROM album
																				WHERE album_title='Results_May_Vary')), ('Let Me Down', 256, (SELECT album_id FROM album
																				WHERE album_title='Results_May_Vary')), ('Love Somebody', 229, (SELECT album_id FROM album
																				WHERE album_title='Overexposed')), ('Payphone', 231, (SELECT album_id FROM album
																				WHERE album_title='Overexposed')), ('Circles', 214, (SELECT album_id FROM album
																				WHERE album_title='Hollywood’s_Bleeding')), ('Allergic', 156, (SELECT album_id FROM album
																				WHERE album_title='Hollywood’s_Bleeding')), ('Dark Necessities', 302, (SELECT album_id FROM album
																				WHERE album_title='The_Getaway')), ('The Getaway', 250, (SELECT album_id FROM album
																				WHERE album_title='The_Getaway')), ('Californication', 329, (SELECT album_id FROM album
																				WHERE album_title='Californication')), ('Scar Tissue', 215, (SELECT album_id FROM album
																				WHERE album_title='Californication')), ('In my feelings', 136, (SELECT album_id FROM album
																				WHERE album_title='Scorpion')); 

INSERT INTO collection  (collection_title, realese_year) VALUES ('Greatest Hits', 2003), ('collection#1', 2018), ('collection#2', 2019), ('collection#3', 2020),
																('collection#4', 2021), ('collection#5', 2022), ('collection#6', 2015), ('collection#7', 2016);
															
INSERT INTO artist_album (artist_id, album_id) VALUES ((SELECT artist_id FROM artist WHERE artist_name='ASAP Rocky'), (SELECT album_id FROM album WHERE album_title='At._Long._Last._ASAP')),
		((SELECT artist_id FROM artist WHERE artist_name='ASAP Rocky'), (SELECT album_id FROM album WHERE album_title='Testing')),
		((SELECT artist_id FROM artist WHERE artist_name='Drake'), (SELECT album_id FROM album WHERE album_title='Certified_Lover_Boy')),
		((SELECT artist_id FROM artist WHERE artist_name='Drake'), (SELECT album_id FROM album WHERE album_title='Scorpion')),
		((SELECT artist_id FROM artist WHERE artist_name='Drake'), (SELECT album_id FROM album WHERE album_title='Views')),
		((SELECT artist_id FROM artist WHERE artist_name='Imagine Dragons'), (SELECT album_id FROM album WHERE album_title='Evolve')),
		((SELECT artist_id FROM artist WHERE artist_name='Kendrick Lamar'), (SELECT album_id FROM album WHERE album_title='DAMN.')),
		((SELECT artist_id FROM artist WHERE artist_name='Limp Bizkit'), (SELECT album_id FROM album WHERE album_title='Results_May_Vary')),
		((SELECT artist_id FROM artist WHERE artist_name='Maroon 5'), (SELECT album_id FROM album WHERE album_title='Overexposed')),
		((SELECT artist_id FROM artist WHERE artist_name='Post Malone'), (SELECT album_id FROM album WHERE album_title='Hollywood’s_Bleeding')),
		((SELECT artist_id FROM artist WHERE artist_name='Red Hot Chili Peppers'), (SELECT album_id FROM album WHERE album_title='The_Getaway')),
		((SELECT artist_id FROM artist WHERE artist_name='Red Hot Chili Peppers'), (SELECT album_id FROM album WHERE album_title='Californication')),
		((SELECT artist_id FROM artist WHERE artist_name='ASAP Rocky'), (SELECT album_id FROM album WHERE album_title='Scorpion'));

INSERT INTO artist_genre (artist_id, genre_id) VALUES ((SELECT artist_id FROM artist WHERE artist_name='ASAP Rocky'), (SELECT genre_id FROM genre WHERE genre_name='R&B')),
		((SELECT artist_id FROM artist WHERE artist_name='ASAP Rocky'), (SELECT genre_id FROM genre WHERE genre_name='Hip-hop')),
		((SELECT artist_id FROM artist WHERE artist_name='ASAP Rocky'), (SELECT genre_id FROM genre WHERE genre_name='Rap')),
		((SELECT artist_id FROM artist WHERE artist_name='Drake'), (SELECT genre_id FROM genre WHERE genre_name='R&B')),
		((SELECT artist_id FROM artist WHERE artist_name='Drake'), (SELECT genre_id FROM genre WHERE genre_name='Hip-hop')),
		((SELECT artist_id FROM artist WHERE artist_name='Drake'), (SELECT genre_id FROM genre WHERE genre_name='Rap')),
		((SELECT artist_id FROM artist WHERE artist_name='Post Malone'), (SELECT genre_id FROM genre WHERE genre_name='R&B')),
		((SELECT artist_id FROM artist WHERE artist_name='Post Malone'), (SELECT genre_id FROM genre WHERE genre_name='Hip-hop')),
		((SELECT artist_id FROM artist WHERE artist_name='Imagine Dragons'), (SELECT genre_id FROM genre WHERE genre_name='Pop-rock')),
		((SELECT artist_id FROM artist WHERE artist_name='Kendrick Lamar'), (SELECT genre_id FROM genre WHERE genre_name='Hip-hop')),
		((SELECT artist_id FROM artist WHERE artist_name='Kendrick Lamar'), (SELECT genre_id FROM genre WHERE genre_name='Rap')),
		((SELECT artist_id FROM artist WHERE artist_name='Limp Bizkit'), (SELECT genre_id FROM genre WHERE genre_name='Alternative')),
		((SELECT artist_id FROM artist WHERE artist_name='Limp Bizkit'), (SELECT genre_id FROM genre WHERE genre_name='Rap')),
		((SELECT artist_id FROM artist WHERE artist_name='Maroon 5'), (SELECT genre_id FROM genre WHERE genre_name='Pop-rock')),
		((SELECT artist_id FROM artist WHERE artist_name='Red Hot Chili Peppers'), (SELECT genre_id FROM genre WHERE genre_name='Funk-rock'));
		
INSERT INTO track_collection (track_id, collection_id) VALUES ((SELECT track_id FROM track WHERE track_title='Californication'),(SELECT collection_id FROM collection WHERE collection_title='Greatest Hits')),
			((SELECT track_id FROM track WHERE track_title='Scar Tissue'),(SELECT collection_id FROM collection WHERE collection_title='Greatest Hits')),
			((SELECT track_id FROM track WHERE track_title='LSD'),(SELECT collection_id FROM collection WHERE collection_title='collection#1')),
			((SELECT track_id FROM track WHERE track_title='Champagne Poetry'),(SELECT collection_id FROM collection WHERE collection_title='collection#1')),
			((SELECT track_id FROM track WHERE track_title='No Friends In the Industry'),(SELECT collection_id FROM collection WHERE collection_title='collection#1')),
			((SELECT track_id FROM track WHERE track_title='No Friends In the Industry'),(SELECT collection_id FROM collection WHERE collection_title='collection#2')),
			((SELECT track_id FROM track WHERE track_title='DNA'),(SELECT collection_id FROM collection WHERE collection_title='collection#2')),
			((SELECT track_id FROM track WHERE track_title='DNA'),(SELECT collection_id FROM collection WHERE collection_title='collection#1')),
			((SELECT track_id FROM track WHERE track_title='No Friends In the Industry'),(SELECT collection_id FROM collection WHERE collection_title='collection#3')),
			((SELECT track_id FROM track WHERE track_title='Loyalty'),(SELECT collection_id FROM collection WHERE collection_title='collection#3')),
			((SELECT track_id FROM track WHERE track_title='Humble'),(SELECT collection_id FROM collection WHERE collection_title='collection#4')),
			((SELECT track_id FROM track WHERE track_title='DNA'),(SELECT collection_id FROM collection WHERE collection_title='collection#4')),
			((SELECT track_id FROM track WHERE track_title='Circles'),(SELECT collection_id FROM collection WHERE collection_title='collection#5')),
			((SELECT track_id FROM track WHERE track_title='Circles'),(SELECT collection_id FROM collection WHERE collection_title='collection#2')),
			((SELECT track_id FROM track WHERE track_title='Allergic'),(SELECT collection_id FROM collection WHERE collection_title='collection#5')),
			((SELECT track_id FROM track WHERE track_title='Allergic'),(SELECT collection_id FROM collection WHERE collection_title='collection#6')),
			((SELECT track_id FROM track WHERE track_title='Tony Tone'),(SELECT collection_id FROM collection WHERE collection_title='collection#6')),
			((SELECT track_id FROM track WHERE track_title='Tony Tone'),(SELECT collection_id FROM collection WHERE collection_title='collection#7')),
			((SELECT track_id FROM track WHERE track_title='Survival'),(SELECT collection_id FROM collection WHERE collection_title='collection#7')),
			((SELECT track_id FROM track WHERE track_title='Survival'),(SELECT collection_id FROM collection WHERE collection_title='collection#3'));