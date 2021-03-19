SET SEARCH_PATH TO parlgov;
drop table if exists q5 cascade;

-- You must not change this table definition.

CREATE TABLE q5(
electionId INT,
countryName VARCHAR(50),
winningParty VARCHAR(100),
closeRunnerUp VARCHAR(100)
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

--From election result extract other winners who have the same alliance id as null winners id. This includes null winners themselves. #44
create view winner_part1 as
select e.election_id, e.id, e.party_id, e.alliance_id, n.country_id
from election_result e, null_winners n
where e.alliance_id = n.id;

--Find all other players who share the same winner id (from alliance_id) in the same election. #183
create view winner_part2 as
select w2.election_id, w2.id, w2.party_id, w1.alliance_id, w1.country_id
from other_winners w1, election_result w2
where (w1.election_id = w2.election_id) and (w1.alliance_id = w2.alliance_id or w1.alliance_id = w2.id);

-- #320
create view total_winners as
(select *
from null_winners) union
(select * from winner_part1) union
(select * from winner_part2);

-- votes count for each winner party
create view winner_count as
select election_id, total_winners.id, party_id, alliance_id, total_winners.country_id, votes_valid
from total_winners join election on total_winners.election_id = election.id and total_winners.country_id = election.country_id;

-- total votes for each winner party or alliance.
create view total_winner_count1 as
select alliance_id, sum(votes_valid) as count
from winner_count
group by alliance_id;


-- more info for winners
create view total_winner_count as
select *
from total_winners natural join total_winner_count1;


-- part1 election PE(null alliance_id) players.
Create view p1 as
select election_id, election_result.id, party_id, election_result.id as alliance_id, country_id
from election_result join election on election.id = election_result.election_id
where alliance_id IS NULL and election.e_type = 'Parliamentary election';

-- part2 election PE(not null alliance_id) players.
Create view p2 as
select election_id, election_result.id, party_id, alliance_id, country_id
from election_result join election on election.id = election_result.election_id
where alliance_id IS NOT NULL and election.e_type = 'Parliamentary election';

-- All election PE players.
Create view a1 as
(select * from p1) union (select * from p2);

-- Election PE players except winner parties.
Create view normal_p as
(select * from a1) except (select * from total_winners);

-- votes count for each normal party
create view normal_count as
select election_id, normal_p.id, party_id, alliance_id, normal_p.country_id, votes_valid
from normal_p join election on normal_p.election_id = election.id and normal_p.country_id = election.country_id;

-- total votes for each normal party or alliance.
create view total_normal_count1 as
select alliance_id, sum(votes_valid) as count
from normal_count
group by alliance_id;

-- More info on normal party
create view total_normal_count as
select *
from total_normal_count1 natural join normal_p;


-- Normal players with votes within 10% less than the winner party. CHECKCHECK INEQUALITY
create view max_vote as
select election_id, max(count) as count
from total_normal_count n
group by election_id;

-- Check for close runner_up
create view close_runner as
select w.id
from total_winner_count w natural join max_vote m
where m.count < w.count and m.count >= w.count*0.9;


-- the answer to the query
insert into q5
