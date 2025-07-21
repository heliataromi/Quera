SELECT
    DISTINCT question_id,
    TIMESTAMPDIFF(SECOND, questions.creation_date, b.creation_date) AS time_to_answer
FROM
    questions
JOIN
    (SELECT
        MIN(a.creation_date) AS creation_date,
        a.question_id
    FROM
        answers a
    GROUP BY
        a.question_id) b ON questions.id = b.question_id
ORDER BY
    time_to_answer DESC
LIMIT
    500;