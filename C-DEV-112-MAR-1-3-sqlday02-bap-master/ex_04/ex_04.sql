SELECT summary AS 'Summaries',id FROM movies WHERE (id % 2) = 1 AND id BETWEEN 42 AND 84;
