(SELECT
     'cart' AS funnel_stage,
     FORMAT(COUNT(DISTINCT users.id) / (SELECT COUNT(*) FROM users), 4) AS conversion_rate
FROM
    users
JOIN
    carts ON users.id = carts.user_id)
UNION
(SELECT
     'payment' AS funnel_stage,
     FORMAT(COUNT(DISTINCT users.id) / (SELECT COUNT(*) FROM users), 4) AS conversion_rate
FROM
    users
JOIN
    carts ON users.id = carts.user_id
JOIN
    payments ON carts.id = payments.cart_id);
