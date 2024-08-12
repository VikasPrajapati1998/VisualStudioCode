select * from student 
where city in (select city from student where city="Delhi");
