SELECT 
    p.product_id, 
    IFNULL(ROUND(SUM(p.price * u.units) / NULLIF(SUM(u.units), 0), 2), 0) AS average_price
FROM 
    Prices AS p
LEFT JOIN 
    UnitsSold AS u ON p.product_id = u.product_id 
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY 
    p.product_id;
