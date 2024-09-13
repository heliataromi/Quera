(SELECT job_id,
        squad_id,
        SUM(salary) AS salary
FROM employees
GROUP BY job_id,
         squad_id)

UNION ALL

(SELECT job_id,
        NULL as squad_id,
        SUM(salary) AS salary
FROM employees
GROUP BY job_id)

UNION ALL

(SELECT NULL AS job_id,
        squad_id,
        SUM(salary) AS salary
FROM employees
GROUP BY squad_id)

UNION ALL

(SELECT NULL AS job_id,
        NULL AS squad_id,
        SUM(salary) as salary
FROM employees)

ORDER BY CASE
        WHEN ISNULL(job_id) AND ISNULL(squad_id) THEN 3
        WHEN ISNULL(job_id) THEN 2
        WHEN ISNULL(squad_id) THEN 1
        ELSE 0
    END,
    job_id,
    squad_id;