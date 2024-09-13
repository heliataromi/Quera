-- Section1
SELECT name, year_of_release, global_sales * 1000000 AS global_sales
FROM games
WHERE global_sales >= 20
ORDER BY year_of_release DESC, global_sales DESC
LIMIT 10;

-- Section2
SELECT publisher
FROM games
GROUP BY publisher
ORDER BY SUM(global_sales) DESC
LIMIT 1;

-- Section3
SELECT IF(ISNULL(genre), 'OTHER', genre) AS genre
FROM games
GROUP BY genre
ORDER BY SUM(other_sales) DESC
LIMIT 1;

-- Section4
SELECT name, year_of_release, other_sales, global_sales
FROM games
ORDER BY CASE
        WHEN year_of_release >= 2000 THEN 0
        WHEN year_of_release < 2000 THEN 1
    END,
    CASE
        WHEN year_of_release >= 2000 THEN global_sales
        WHEN year_of_release < 2000 THEN other_sales
    END DESC, id;
