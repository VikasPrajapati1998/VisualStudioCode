/*
MySQL Delete Statement
*/
use demodb;
/*
insert into student(roll, class, name, fatherName, motherName, address, pin, mobileNumber, city)
values (43, "12th", "Aryan Singh", "Arjun Prajapati", "Pihu Chaubey", "Maharua, Akbarpur, Ambedkar Nagar", "224168", "9555366649", "Ayodhya"),
(44, "11th", "Sudhanshu Mishra", "Ghanshyam Mishra", "Anamika Dubey", "Bikapur, Akbarpur", "224149", "6394525157", "Ayodhya");
*/

select * from student;
Delete from student where roll = 11;
select * from student where city = "Navi Mumbai";
select * from student;

