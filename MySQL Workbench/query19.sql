select *, concat_ws(', ', address, city) AS Address from student;
select name as "Student_Name", mobileNumber as "Student_Contact" from student;

select s.roll, s.name as "Student", s.city as "City", t.name as "Teacher" from student as s, teacher as t
where s.name like '%a' and s.roll = t.id;

select student.name as "Student", teacher.name as "Teacher"
from student inner join teacher on student.city = teacher.city;

select student.name as "Student", teacher.name as "Teacher"
from student left join teacher on student.city = teacher.city;

select student.name as "Student", teacher.name as "Teacher"
from student right join teacher on student.city = teacher.city;

select student.name as "Student", teacher.name as "Teacher"
from student cross join teacher on student.city = teacher.city;

select s.name as "Student Name", t.name as "Teacher Name", s.city
from student as s, teacher as t
where student.roll <> teacher.id
and s.city = t.city order by s.city;


