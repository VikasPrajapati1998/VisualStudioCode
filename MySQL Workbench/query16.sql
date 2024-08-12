select * from student where roll >= 10 limit 10 offset 5;
select min(roll) from student where city = "Delhi";
select max(roll) from student where city = "Delhi";
select avg(roll) from student where city = "Delhi";
select sum(roll) from student where city = "Delhi";
select count(roll) from student where city = "Delhi";
select city from student where city like "%_i";
select city from student where city like "%_a_";
select city from student where city like "%a";
select city from student where city not like "%a";
select city from student where city like "D_l_i"
