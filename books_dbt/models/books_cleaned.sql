SELECT title, price,
    CASE rating
        WHEN 'One' THEN 1
        WHEN 'Two' THEN 2
        WHEN 'Three' THEN 3
        WHEN 'Four' THEN 4
        WHEN 'Five' THEN 5
    END AS rating_num
FROM books_raw