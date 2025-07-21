SELECT
    students.*
FROM students
LEFT JOIN
    student_courses sc ON students.id = sc.student_id AND sc.course_id = 7
WHERE course_id IS NULL;