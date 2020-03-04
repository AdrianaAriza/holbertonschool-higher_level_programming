--
--
SELECT tv_genres.name FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
FULL OUTER JOIN tv_genres ON tv_show_genres.show_id = tv_genres.id
WHERE tv_shows.id = 8
ORDER BY tv_genres.name;
