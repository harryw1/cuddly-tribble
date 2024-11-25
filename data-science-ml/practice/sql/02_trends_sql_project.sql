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

select avg(valuation)
from startups;

select round(avg(valuation),2)
from startups
group by category;

select category, round(avg(valuation),2)
from startups
group by category
order by avg(valuation) desc;

select category, count(category)
from startups
group by category
having count(category) >= 3;
