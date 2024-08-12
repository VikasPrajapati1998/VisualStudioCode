-- select * from student
-- where name = ALL (select name from student where roll = 10)

select * from student
where name = Any (select name from student 
					where roll >= 10 and roll <= 20);
