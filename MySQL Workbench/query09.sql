use arjundb;
select * from student limit 5;
select * from student where class = "11th";
select distinct class from student;
select count(distinct class) from student;
select count(distinct roll) from student;
select * from student where roll >= 10 and roll <= 30;
select * from student where roll between 10 and 30;
select * from student where name like '%r';
select * from student where name like 'R%';
select * from student where name like '%m%';
select * from student where roll in (10, 20, 30, 40, 50);

