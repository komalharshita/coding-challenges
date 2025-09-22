SELECT sit
FROM ministers
WHERE 
    (is_next_gov = 'yes' OR is_next_gov = '1')
    AND (is_spoke_bad = 'no' OR is_spoke_bad = '0')
    AND sit % 2 = 0
ORDER BY sit;