-- Section1
    SELECT name
    FROM athletes
    WHERE nationality = 'Islamic Republic of Iran'
    ORDER BY name;

-- Section2
    SELECT discipline, nationality, count(*) AS count
    FROM athletes
    GROUP BY discipline, nationality
    ORDER BY count(name) DESC;

-- Section3
    SELECT nationality, count(*) AS count
    FROM athletes
    GROUP BY nationality
    ORDER BY count(name) DESC;
