SELECT id, name
FROM events

WHERE size > 100 or size < 1 or year < 2000 or name is null
order by id desc ;
