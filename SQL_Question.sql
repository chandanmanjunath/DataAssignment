select e.*
from (select e.*, count(*) over (partition by group_val) as people
      from (select e.*,
                   sum(case when people_count < 100 then 1 else 0 end) over (order by eventname) as group_val
            from test_event e
           ) e
     ) e
where people >= 3;
