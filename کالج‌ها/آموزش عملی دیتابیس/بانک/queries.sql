-- Section1
SELECT ACCOUNT_NO
FROM accounts
GROUP BY ACCOUNT_NO
ORDER BY COUNT(ACCOUNT_NO) DESC;

-- Section2
SELECT YEAR(DATE), DATE
FROM accounts
GROUP BY DATE
HAVING COUNT(DATE) > 10
ORDER BY COUNT(DATE) DESC;

-- Section3
SELECT a.ACCOUNT_NO, MIN(a.BALANCE) AS BALANCE
FROM accounts a,
     (SELECT ACCOUNT_NO, MAX(DATE) AS MAX_DATE
      FROM accounts
      GROUP BY ACCOUNT_NO) b
WHERE a.ACCOUNT_NO = b.ACCOUNT_NO
      AND a.DATE = b.MAX_DATE
      AND a.BALANCE < -1000000000
GROUP BY a.ACCOUNT_NO
ORDER BY BALANCE;

-- Section4
START TRANSACTION;
INSERT INTO accounts
VALUES (45532, NOW(), 1000000, 0, (SELECT BALANCE
                                                                            FROM accounts
                                                                            WHERE ACCOUNT_NO = 45532
                                                                            ORDER BY DATE DESC
                                                                            LIMIT 1) - 1000000
       );
INSERT INTO accounts
VALUES (32124, NOW(), 0, 1000000, (SELECT BALANCE
                                                                            FROM accounts
                                                                            WHERE ACCOUNT_NO = 45532
                                                                            ORDER BY DATE DESC
                                                                            LIMIT 1) + 1000000
       );
COMMIT;