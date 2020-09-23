SET SEARCH_PATH TO parlgov;
drop table if exists q7 cascade;

-- You must not change this table definition.

DROP TABLE IF EXISTS q7 CASCADE;
CREATE TABLE q7(
partyId INT,
partyFamily VARCHAR(50)
);

-- You may find it convenient to do this for each of the views
-- that define your intermediate steps.  (But give them better names!)
DROP VIEW IF EXISTS intermediate_step CASCADE;

-- Define views for your intermediate steps here.
create view duplicate_election_winners as
select election.id as election_id, cabinet_party.party_id, cabinet.country_id
from election join cabinet on election.id = cabinet.election_id
join cabinet_party on cabinet.id = cabinet_party.cabinet_id
where cabinet_party.pm = true and election.e_type = 'Parliamentary election';

-- unique election winners (#181)
create view election_winners as
(select * from duplicate_election_winners) union (select * from duplicate_election_winners);

--(171)
--Find the partial winners with alliances info (why # of lines in all winners < # of line in election winners?)
create view all_winners as
select election_winners.election_id, election_result.id, election_winners.party_id, election_result.alliance_id, election_winners.country_id
from election_winners join election_result on election_winners.election_id = election_result.election_id
and election_winners.party_id = election_result.party_id;

--Null winners
create view null_winners as
select election_id, id, party_id, id as alliance_id, country_id
from all_winners
where alliance_id is NULL;

create view other_winners as
select *
from all_winners
where alliance_id IS NOT NULL;

--From election result extract other winners who have the same alliance id as null winners id. This includes null winners themselves.
create view winner_part1 as
select e.election_id, e.id, e.party_id, e.alliance_id, n.country_id
from election_result e, null_winners n
where e.alliance_id = n.id;

--Find all other players who share the same winner id (from alliance_id) in the same election.
create view winner_part2 as
select w2.election_id, w2.id, w2.party_id, w1.alliance_id, w1.country_id
from other_winners w1, election_result w2
where (w1.election_id = w2.election_id) and (w1.alliance_id = w2.alliance_id or w1.alliance_id = w2.id);

-- #320 rows
create view total_winners as
(select *
from null_winners) union
(select * from winner_part1) union
(select * from winner_part2);

create view party_id_and_date as
select t.party_id, e.e_date as date, election_id
from total_winners t, election e
where t.election_id = e.id
order by party_id;

-- get the European Parliament information, #24 rows
create view ep_election as
select id, e_date as date
from election
where e_type = 'European Parliament';

-- find the party once served before first EP election, #279
create view temp_1 as
select *
from party_id_and_date
where party_id in (select party_id from party_id_and_date where date < (select min(date) from ep_election));

-- filter out the winning record from above view which occurs after last EP election, #275
create view temp_2 as
select *
from temp_1
where date < (select max(date) from ep_election);

-- combine temp_2 with corresponding previous ep elections
create view temp_3 as
select t.party_id, t.date, t.election_id, e.previous_ep_election_id
from temp_2 t, election e
where t.election_id = e.id
order by party_id;

-- count # of distinct previous ep elction for each party
create view temp_4 as
select party_id, count(distinct previous_ep_election_id) from temp_3 group by party_id;

-- find the strong parties
create view strong_party as
select party_id
from temp_4
where count = (select count(date) -1 from ep_election);

create view solution as
select strong_party.party_id as partyID, party_family.family as partyFamily
from strong_party left join party_family on strong_party.party_id = party_family.party_id;


-- the answer to the query
insert into q7 select * from solution;
