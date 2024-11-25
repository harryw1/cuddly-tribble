select * from trips;
select * from riders;
select * from cars;

select *
from riders
cross join cars;

select *
from trips
left join riders
  on trips.rider_id = riders.id
group by riders.id
order by riders.id;

select *
from trips
inner join cars
  on trips.car_id = cars.id;

select *
from riders
UNION
select *
from riders2;

select round(avg(cost), 2)
from trips;

select distinct username
from riders
where total_trips < 500;

select count(*)
from cars
where status = 'active';

select id
from cars
order by trips_completed desc
limit 2;
