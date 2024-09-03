-- Section1
    DELETE FROM users
    WHERE family NOT LIKE '%m%' AND family NOT LIKE '%d%';
-- Section2
    DELETE FROM users
    WHERE family = 'mohammadi' OR salary IN(7356, 9701, 2885, 7414, 3801);
-- Section3
    DELETE FROM users
    WHERE family = 'booazar' OR users.birth_date BETWEEN '1995-01-01' AND '2000-12-31';
