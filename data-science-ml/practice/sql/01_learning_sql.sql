select *
from nomnom;

select distinct neighborhood
from nomnom;

select distinct cuisine
from nomnom;

select distinct name
from nomnom
where cuisine = 'Chinese';

select distinct name
from nomnom
where review >= 4;

select distinct name
from nomnom
where cuisine = 'Italian' and price = '$$$';

select distinct name
from nomnom
where name like '%meatball%';

select distinct name
from nomnom
where neighborhood = 'Downtown' or neighborhood = 'Midtown' or neighborhood = 'Chinatown';

select distinct name
from nomnom
where health = NULL;

select distinct name
from nomnom
order by review desc
limit 10;

select *,
    case
        when review >= 4 then 'Great'
        when review >= 3 then 'Good'
        when review >= 2 then 'Fair'
        when review >= 1 then 'Poor'
        else 'Terrible'
    end as 'Rating'
from nomnom;
