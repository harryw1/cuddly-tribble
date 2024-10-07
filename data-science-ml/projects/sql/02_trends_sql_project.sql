select *
from startups;

select count(distinct name)
from startups;

select sum(valuation)
from startups;

select max(raised)
from startups;

select max(raised)
from startups
where stage = 'Seed';

select name
from startups
order by founded
limit 1;

select min(founded)
from startups;
