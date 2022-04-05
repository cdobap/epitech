SELECT COUNT(*) AS 'Number of movies that starts with "eX"' FROM movies WHERE REGEXP_LIKE(title, '^eX', 'c');
