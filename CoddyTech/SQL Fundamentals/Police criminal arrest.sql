select top 5 name as worst_criminals
from police_report
where ( report is null OR report LIKE '%g%' OR report LIKE '%b%' OR report LIKE '%G%' OR report LIKE '%B%' )
    and map in ('Caerleon', 'Dewsbury', 'Kirekwall', 'Findochty')
order by severe_score desc;