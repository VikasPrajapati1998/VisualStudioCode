use demodb;
select * from student;
select distinct city from student;
select count(distinct city) as City_Count from student;
select * from student
where city = 'Delhi' or (city = 'Noida' or city = 'Gurgaon');
select * from student order by city ASC;
select * from student order by city DESC;
select * from student order by name ASC, fatherName DESC;



