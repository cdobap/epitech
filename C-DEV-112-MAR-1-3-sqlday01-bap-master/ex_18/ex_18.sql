SELECT CONCAT(UPPER(LEFT(lastname, 1)), SUBSTRING(lastname, 2), '.', UPPER(LEFT(firstname, 1)), SUBSTRING(firstname, 2)) AS 'Full name' FROM profiles ORDER BY birthdate DESC;
