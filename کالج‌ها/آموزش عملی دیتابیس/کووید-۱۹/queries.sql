-- Section1
    SELECT country, sum(new_cases) AS total_case, sum(new_deaths) AS total_death
    FROM covid
    GROUP BY country
    ORDER BY total_death DESC;

-- Section2
    SELECT sum(new_cases) AS total_case, sum(new_deaths) AS total_death
    FROM covid
    WHERE country = 'Iran (Islamic Republic of)';

-- Section3
    SELECT country, rank()
    OVER (ORDER BY sum(new_deaths) DESC )
    AS `rank`
    FROM covid
    GROUP BY country
    ORDER BY `rank`;

    -- Section4
    SELECT `rank`
    FROM (SELECT country, rank()
        OVER (ORDER BY sum(new_deaths) DESC )
        AS `rank`
        FROM covid
        GROUP BY country
        ORDER BY `rank`) as cr
    WHERE country = 'Iran (Islamic Republic of)';
