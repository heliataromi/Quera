WITH RECURSIVE ancestors_cte AS
(
  SELECT id, title, slug, parent_id, 0 AS depth
  FROM categories
  WHERE id = 741
  UNION ALL
  SELECT c.id, c.title, c.slug, c.parent_id, a.depth + 1
  FROM categories c
  JOIN ancestors_cte a ON c.id = a.parent_id
)
SELECT title, slug
FROM ancestors_cte
ORDER BY depth DESC;
