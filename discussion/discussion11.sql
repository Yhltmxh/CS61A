
drop table if exists pizzas;
drop table if exists meals;

CREATE TABLE pizzas AS
  SELECT "Artichoke" AS name, 12 AS open, 15 AS close UNION
  SELECT "La Val's"         , 11        , 22          UNION
  SELECT "Sliver"           , 11        , 20          UNION
  SELECT "Cheeseboard"      , 16        , 23          UNION
  SELECT "Emilia's"         , 13        , 18;

CREATE TABLE meals AS
  SELECT "breakfast" AS meal, 11 AS time UNION
  SELECT "lunch"            , 13         UNION
  SELECT "dinner"           , 19         UNION
  SELECT "snack"            , 22;
  
-- Q1: Open Early
select name from pizzas where open < 13 order by name desc;


-- Q2: Study Session
create table study as
    select name, max(14 - open, 0) as duration from pizzas order by duration desc;

select * from study;

-- Q3: Late Night Snack
create table late as
    select name || " closes at " || close as status from pizzas where close > 21;

select * from late;

-- Q4: Double Pizza
create table double as
    select a.meal, b.meal, c.name from meals as a, meals as b, pizzas as c
        where b.time - a.time > 6 
            and a.time >= c.open and a.time <= c.close
            and b.time >= c.open and b.time <= c.close;

select * from double;
    
