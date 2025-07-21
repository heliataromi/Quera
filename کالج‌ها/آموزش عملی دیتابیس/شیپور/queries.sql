-- Section1
SELECT c.Name
FROM advertisements AS a
JOIN categories c ON c.ID = a.IDCategory
WHERE c.IDParent IS NULL
GROUP BY c.Name
ORDER BY COUNT(*) DESC
LIMIT 1;


-- Section2
SELECT c.Name
FROM advertisements AS a
JOIN categories c ON c.ID = a.IDCategory
WHERE c.IDParent IS NOT NULL AND YEAR(a.DateAdded) = 2016 AND MONTH(a.DateAdded) = 2
GROUP BY c.Name
ORDER BY COUNT(*) DESC
LIMIT 1;

-- Section3
WITH count_categories AS (
    SELECT IDUser, COUNT(IDCategory) as CountCategories
    FROM advertisements
    GROUP BY IDUser
    HAVING CountCategories = 1
)
SELECT COUNT(IDUser)
FROM count_categories;


-- Section4
SELECT IDUser,
       COUNT(IDCategory) OVER (
            PARTITION BY IDUser
            ORDER BY DateAdded
            RANGE BETWEEN INTERVAL 30 DAY PRECEDING AND CURRENT ROW) total_ads
FROM advertisements
ORDER BY total_ads DESC
LIMIT 1;

-- Section5
WITH estate_categories AS (
    SELECT IDUser,
           DateAdded,
           Price,
           IDCategory,
           Name
    FROM advertisements
    JOIN categories
    ON advertisements.IDCategory = categories.ID
    WHERE Name LIKE '%Estate%'
)
SELECT IDUser
FROM estate_categories
ORDER BY COUNT(IDCategory) OVER (
            PARTITION BY IDUser
            ORDER BY DateAdded
            RANGE BETWEEN INTERVAL 30 DAY PRECEDING AND CURRENT ROW) DESC,
         Price DESC
LIMIT 1;

-- Section6
WITH car_categories AS (
    SELECT DateAdded,
           Price,
           IDCategory
    FROM advertisements
    JOIN categories
    ON advertisements.IDCategory = categories.ID
    WHERE Name LIKE '%car%'
)
SELECT IDCategory
FROM car_categories
WINDOW YearWindow AS (
        PARTITION BY IDCategory
        ORDER BY DateAdded
        RANGE BETWEEN INTERVAL 1 YEAR PRECEDING AND CURRENT ROW
    )
ORDER BY MAX(Price) OVER YearWindow - MIN(Price) OVER YearWindow DESC
LIMIT 1;
