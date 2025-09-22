SELECT id AS to_renew
FROM beverages
WHERE 
    current_year - expiration_year > 6
    OR expiration_year = current_year
    OR expiration_year = current_year + 1
ORDER BY current_year - expiration_year DESC;