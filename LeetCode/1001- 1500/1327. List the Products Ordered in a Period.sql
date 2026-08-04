SELECT p.product_name, SUM(o.unit) as unit
FROM Products p
JOIN Orders o
ON p.product_id = o.product_id
WHERE o.order_date LIKE '2020-02-%'
GROUP BY p.product_id
HAVING unit >= 100 ;
