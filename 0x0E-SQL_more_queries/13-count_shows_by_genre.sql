-- List shows linked to database
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows
FROM tv_show_genres
WHERE tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_shows DESC;
