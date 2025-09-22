select model as id
from cellphones
where (price between 1000 and 1500) and (wifi_5g is true) and ( model like 'm_o%') ;

