SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;

select sum(score)
from hacker_news;

select user, sum(score)
from hacker_news
group by user
having sum(score) > 200
order by 2 desc;

select (309+304+282+517)/6366.0;

select user, count(*)
from hacker_news
where url like '%dQw4w9WgXcQ%'
group by user;

select case
  when url like '%github.com%' then 'GitHub'
  when url like '%medium.com%' then 'Medium'
  when url like '%nytimes.com%' then 'NYT'
  else 'Other'
  end as 'Source',
  count(*)
from hacker_news
group by 1
order by 2 desc;

select timestamp
from hacker_news
limit 10;

select timestamp,
  strftime('%H', timestamp)
from hacker_news
group by 1
limit 20;

select strftime('%H', timestamp) as 'Time',
  round(avg(score), 2) as 'Score',
  count(title) as 'Num Posts'
from hacker_news
where timestamp is not null
group by 1
order by 2 desc;
