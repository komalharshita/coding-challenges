SELECT seat_id
FROM (
    SELECT *, LAG(free) OVER(ORDER BY seat_id) AS befor,
            LEAD(free) OVER (ORDER BY seat_id) AS after
    FROM Cinema
) T
WHERE (free = 1 AND befor = 1) OR (free = 1 AND after = 1)
ORDER BY seat_id ;