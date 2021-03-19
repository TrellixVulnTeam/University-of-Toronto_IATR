SET SEARCH_PATH TO parlgov;
drop table if exists q2 cascade;

-- You must not change this table definition.

create table q2(
country VARCHAR(50),
electoral_system VARCHAR(100),
single_party INT,
two_to_three INT,
four_to_five INT,
six_or_more INT
);


-- You may find it convenient to do this for each of the views
-- that define your intermediate steps.  (But give them better names!)
DROP VIEW IF EXISTS intermediate_step CASCADE;

-- Define views for your intermediate steps here.

-- extract PE winners in election
create view election_winners as
select election.id as election_id, cabinet_party.party_id, cabinet.country_id
from election join cabinet on election.id = cabinet.election_id
join cabinet_party on cabinet.id = cabinet_party.cabinet_id
where cabinet_party.pm = true and election.e_type = 'Parliamentary election';

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

create view total_winners as
(select * from winner_part1) union all
(select * from winner_part2);


create view election_num as
select alliance_id, count(party_id) as count
from total_winners
group by alliance_id;

create view count1 as 
select distinct total_winners.country_id, total_winners.alliance_id
from total_winners join election_num on total_winners.alliance_id = election_num.alliance_id and election_num.count = 1;

create view count23 as 
select distinct total_winners.country_id, total_winners.alliance_id
from total_winners join election_num on total_winners.alliance_id = election_num.alliance_id and (election_num.count = 2 or election_num.count = 3);

create view count45 as 
select distinct total_winners.country_id, total_winners.alliance_id
from total_winners join election_num on total_winners.alliance_id = election_num.alliance_id and (election_num.count = 4 or election_num.count = 5);

create view count6 as 
select distinct total_winners.country_id, total_winners.alliance_id
from total_winners join election_num on total_winners.alliance_id = election_num.alliance_id and election_num.count >=6;

create view country_count1 as
Select country_id, count(count1.alliance_id) as single_party
From country join count1 on country.id = count1.country_id
Group by count1.country_id;

create view country_count23 as
Select country_id, count(count23.alliance_id) as two_to_three
From country join count23 on country.id = count23.country_id
Group by count23.country_id;

create view country_count45 as
Select country_id, count(count45.alliance_id) as four_to_five
From country join count45 on country.id = count45.country_id
Group by count45.country_id;

create view country_count6 as
Select country_id, count(count6.alliance_id) as six_or_more
From country join count6 on country.id = count6.country_id
Group by count6.country_id;

Create view final as
Select country_id, single_party, two_to_three, four_to_five, six_or_more
From country_count1 natural full join country_count23 natural full join country_count45 natural full join country_count6;

Create view new_final as
Select country_id, COALESCE(final.single_party, 0) as single_party, COALESCE(final.two_to_three, 0) as two_to_three, COALESCE(final.four_to_five, 0) as four_to_five, COALESCE(final.six_or_more, 0) as six_or_more
From final;

Create view solution as 
Select country.name as country, country.electoral_system, new_final.single_party, new_final.two_to_three, new_final.four_to_five, new_final.six_or_more
From new_final join country on new_final.country_id = country.id;

-- the answer to the query 
insert into q2 select * from solution;

