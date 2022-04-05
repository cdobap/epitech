SELECT title AS 'Movie title', TIMESTAMPDIFF(DAY, release_date, CURDATE()) AS 'Number of days passed' FROM movies WHERE release_date IS NOT NULL;
