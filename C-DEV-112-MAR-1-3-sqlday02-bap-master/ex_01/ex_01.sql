SELECT COUNT(*) AS 'Number of members', ROUND(AVG(TIMESTAMPDIFF(YEAR, profiles.birthdate, CURDATE()))) AS 'Average age' FROM m
ember INNER JOIN profiles ON member.profile_id = profiles.id;
