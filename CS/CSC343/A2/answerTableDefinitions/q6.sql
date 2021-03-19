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

-- create country_id, party_id, election_id views
create view country_party_election as
select country_id, party_id, election_id
from total_winners
order by country_id, party_id;

-- combine previous pe election information
create view pe_election as
select id, country_id, e_date, previous_parliament_election_id
from election
where e_type = 'Parliamentary election';

-- create all possible TABLE
create view temp_2 as
select c.id as country_id, p.id as election_id, p.e_date as date, party.id as party_id
from country c, pe_election p, party
where c.id = p.country_id and c.id = party.country_id
order by party.id, p.e_date;

create view temp_3 as
select country_id, election_id, party_id, 1 as success
from total_winners;

create view temp_4 as
select *
from temp_2 natural left join temp_3;

create view p as
Select *, (row_number() over (order by country_id, party_id, date) - row_number() over (partition by success order by country_id, party_id, date)) as rnDiff
From temp_4
Order by country_id, party_id, date;

Create view pp as
Select country_id, party_id, date, success, ROW_NUMBER() OVER(PARTITION BY success,rnDiff ORDER BY country_id, party_id, date) AS consecutive
FROM p
Order by country_id, party_id, date;

Create view filter_success as
Select country_id, party_id, date, consecutive
From pp
Where success IS NOT NULL;

Create view max_pvotes as
Select country_id, max(consecutive) as max
From filter_success
Group by country_id;

Create view max_evotes as
Select distinct p.country_id, party_id, max
From max_pvotes p, filter_success s
Where p.country_id = s.country_id and s.consecutive = p.max;

Create view solution as
Select m.country_id as countryId, p.name_short as partyName, m.max as number
From max_evotes m, party p
Where m.party_id = p.id and m.country_id = p.country_id;


-- the answer to the query
insert into q6 select * from solution;
