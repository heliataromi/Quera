SELECT DISTINCT users.id,
                users.username
FROM users
JOIN likes
    ON users.id = likes.user_id
WHERE MONTH(likes.created_at) = 10 AND YEAR(likes.created_at) = 2021;
