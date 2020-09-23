SET SEARCH_PATH TO parlgov;
drop table if exists q3 cascade;

-- You must not change this table definition.

create table q3(
country VARCHAR(50),
num_dissolutions INT,
most_recent_dissolution DATE,
num_on_cycle INT,
most_recent_on_cycle DATE
);

-- You may find it convenient to do this for each of the views
-- that define your intermediate steps.  (But give them better names!)
DROP VIEW IF EXISTS intermediate_step CASCADE;

-- Define views for your intermediate steps here.

-- find the elections only for parliamentary elections
create view pe_election as
select id, country_id, e_date, previous_parliament_election_id
from election
where e_type = 'Parliamentary election';

-- create view which contain this election and previous election information
-- and election cycle and country.
create view temp_election_1 as
select pe2.id as election_id, c.id as country_id, pe2.e_date as date, pe1.id as pre_pe_id, pe1.e_date as pre_pe_date, c.election_cycle
from pe_election pe1, pe_election pe2, country c
where pe2.previous_parliament_election_id = pe1.id and pe2.country_id = c.id ;

--get the view which has all first elections
create view temp_election_2 as
select p.id as election_id, c.id as country_id, c.election_cycle
from pe_election p , country c
where (p.previous_parliament_election_id is NULL) and (p.country_id = c.id);

create view temp_election_3 as
select election_id, country_id, extract(year from date) - extract(year from pre_pe_date) as difference, election_cycle
from temp_election_1;

-- create on-cycle views
create view on_cycle as
select election_id, country_id, election_cycle
from temp_election_3
where difference = election_cycle;

-- combine on_cycle with temp_election_2
create view on_cycle_final as
(select * from temp_election_2) union (select * from on_cycle);

create view off_cycle as
select election_id, country_id, election_cycle
from temp_election_3
where election_id not in (select election_id from on_cycle_final);

-- create on_cycle view with DATE
create view on_cycle_real_final as
select o.election_id, o.country_id, p.e_date as date
from on_cycle_final o, pe_election p
where o.election_id = p.id;


-- create off_cycle view with DATE
create view off_cycle_real_final as
select o.election_id, o.country_id, p.e_date as date
from off_cycle o, pe_election p
where o.election_id = p.id;

--do groupby change to on_cycle_real_final
create view res_1 as
select country_id, count(election_id) as num_on_cycle, max(date) as most_recent_on_cycle
from on_cycle_real_final
group by country_id;

--do groupby change to off_cycle_real_final
create view res_2 as
select country_id, count(election_id) as num_dissolutions, max(date) as most_recent_dissolution
from off_cycle_real_final
group by country_id;

-- combine above
create view before_solution as
select *
from res_1  NATURAL FULL JOIN res_2;

create view solution as
select c.name, COALESCE(b.num_dissolutions, 0) as num_dissolutions, b.most_recent_dissolution, COALESCE(b.num_on_cycle,0) as num_on_cycle, b.most_recent_on_cycle
from before_solution b, country c
where b.country_id = c.id;



-- the answer to the query
insert into q3 select * from solution;
