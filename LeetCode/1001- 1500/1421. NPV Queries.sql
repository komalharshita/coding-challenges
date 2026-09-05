SELECT q.id, q.year, IFNULL(n.npv, 0) AS npv
FROM Queries q
LEFT JOIN nvp n
ON q.id = n.id AND q.year = n.year 
ORDER BY q.id ASC ;
