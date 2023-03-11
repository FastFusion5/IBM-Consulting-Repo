SELECT owner_id, owner_name, COUNT(category_title) AS different_category_count
FROM owner O
    JOIN article A ON O.owner_id = A.owner_id
    JOIN category_article_mapping CAM ON A.article_id = CAM.article_id
    JOIN category C ON CAM.category_id = C.category_id
GROUP BY category_title
ORDER BY different_category_count DESC