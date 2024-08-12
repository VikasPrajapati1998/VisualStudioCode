select city from student
union all
select city from teacher;

select city from student
union
select city from teacher;

select count(student.roll), city from student
group by city;

select count(student.roll), city
from student
Having count(student.roll) > 5;

select name from student
where exists (select name from teacher 
where teacher.id = student.roll and id > 5);
