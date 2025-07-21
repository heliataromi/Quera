WITH RECURSIVE ancestors_cte AS
(
    SELECT user_1, user_2, 1 AS degree
    FROM connections
    WHERE user_1 = 256
    UNION ALL
    SELECT c.user_1, c.user_2, degree + 1
    FROM connections c
    JOIN ancestors_cte a ON c.user_1 = a.user_2
)
SELECT degree
FROM ancestors_cte
WHERE user_2 = 512
LIMIT 1;
