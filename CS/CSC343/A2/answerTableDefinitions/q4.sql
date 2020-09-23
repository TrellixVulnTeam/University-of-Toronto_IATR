SET SEARCH_PATH TO parlgov;
drop table if exists q4 cascade;

-- You must not change this table definition.


CREATE TABLE q4(
country VARCHAR(50),
num_elections INT,
num_repeat_party INT,
num_repeat_pm INT
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

-- get all of the winning parties based on the cabinet
create view dup_election_winners as
select election.id as election_id , cabinet_party.party_id
from election join cabinet on election.id = cabinet.election_id join cabinet_party
on cabinet.id = cabinet_party.cabinet_id where cabinet_party.pm = true and election.e_type = 'Parliamentary election';

-- unique election winners (#181)
create view election_winners as
(select * from dup_election_winners) union (select * from dup_election_winners);

-- find all winning parties and previous election winning parties
create view election_winners_pre_winners as
select e1.election_id, e1.party_id, e2.election_id as pre_election_id, e2.party_id as pre_party_id
from pe_election p, election_winners e1, election_winners e2
where e1.election_id = p.id and p.previous_parliament_election_id = e2.election_id;

-- filter above view with same sequential winner party
create view new_election_winners_pre_winners as
select a.election_id, a.party_id, a.pre_party_id
from election_winners_pre_winners a
where a.party_id = a.pre_party_id;

create view num_repeat_party as
select c.name, a.election_id
from new_election_winners_pre_winners a, pe_election b, country c
where a.election_id = b.id and b.country_id = c.id;

-- result of num repeat party!!
create view res_num_repeat_party as
select name as country, count(election_id) as num_repeat_party
from num_repeat_party
group by name;

-- find number of election for each country_id
create view num_elections as
select country_id, count(*) as num_elections
from pe_election
group by country_id;

-- find number of election for each country !!
create view res_num_elections as
select country.name as country, num_elections
from num_elections, country
where num_elections.country_id = country.id;

-- find # of repeat pm
create view pm as
select country_id, regexp_replace(cabinet.name::text, '([A-Za-z]*?)[ IV]+$', '\1') as name
from cabinet;

-- count the # of pm in each country
create view temp as
select name, count(*)
from pm
group by name;

create view new_temp as
select distinct country_id, name
from pm
where name in (select name from temp where count > 1);


create view res_pm as
select country_id, count(*) as num_repeat_pm
from new_temp
group by country_id;

-- create result of pm !!
create view new_res_pm as
select country.name as country, num_repeat_pm
from res_pm, country
where res_pm.country_id = country.id;

create view solution as
select a.country, a.num_elections, b.num_repeat_party, c.num_repeat_pm
from res_num_elections a, res_num_repeat_party b, new_res_pm c
where a.country = b.country and b.country =  c.country;







-- the answer to the query
INSERT INTO q4 select * from solution;
