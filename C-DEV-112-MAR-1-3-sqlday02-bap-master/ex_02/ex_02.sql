SELECT zipcode AS 'Zip codes' FROM profiles GROUP BY zipcode HAVING COUNT(id) > 1 ORDER BY zipcode ASC;
