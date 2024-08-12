use demodb;
create table student(
roll int primary key,
class varchar(50),
name varchar(255),
fatherName varchar(255),
motherName varchar(255),
address varchar(255),
pin varchar(255),
mobileNumber varchar(15)
);

INSERT INTO student (roll, class, name, fatherName, motherName, address, pin, mobileNumber) VALUES
(1, '10th', 'Amit Sharma', 'Rajesh Sharma', 'Sita Sharma', '123 A, Main Street, Delhi', '110001', '9876543210'),
(2, '10th', 'Priya Patel', 'Ramesh Patel', 'Geeta Patel', '456 B, Sector 21, Noida', '201301', '9876543211'),
(3, '11th', 'Rahul Kumar', 'Vikram Kumar', 'Sunita Kumar', '789 C, Phase 3, Gurgaon', '122018', '9876543212'),
(4, '11th', 'Neha Verma', 'Suresh Verma', 'Anita Verma', '101 D, Model Town, Jaipur', '302001', '9876543213'),
(5, '12th', 'Ravi Singh', 'Harish Singh', 'Kavita Singh', '202 E, Block 5, Kanpur', '208001', '9876543214'),
(6, '12th', 'Aisha Khan', 'Mohammed Khan', 'Fatima Khan', '303 F, New Market, Bhopal', '462001', '9876543215'),
(7, '10th', 'Arjun Reddy', 'Ramesh Reddy', 'Laxmi Reddy', '404 G, Green Park, Hyderabad', '500001', '9876543216'),
(8, '10th', 'Sneha Agarwal', 'Anil Agarwal', 'Meena Agarwal', '505 H, Patel Nagar, Mumbai', '400001', '9876543217'),
(9, '11th', 'Rohan Joshi', 'Manoj Joshi', 'Poonam Joshi', '606 I, Lajpat Nagar, Delhi', '110024', '9876543218'),
(10, '11th', 'Maya Kapoor', 'Rajiv Kapoor', 'Neelam Kapoor', '707 J, Shastri Nagar, Ahmedabad', '380001', '9876543219'),
(11, '12th', 'Karan Mehta', 'Sanjay Mehta', 'Seema Mehta', '808 K, Vashi, Navi Mumbai', '400703', '9876543220'),
(12, '12th', 'Sanya Gupta', 'Pankaj Gupta', 'Rekha Gupta', '909 L, MG Road, Bangalore', '560001', '9876543221'),
(13, '10th', 'Ishaan Singh', 'Jitendra Singh', 'Aarti Singh', '1010 M, Sarita Vihar, Delhi', '110076', '9876543222'),
(14, '10th', 'Ritika Nair', 'Krishna Nair', 'Suman Nair', '1111 N, Kamla Nagar, Mumbai', '400039', '9876543223'),
(15, '11th', 'Vikas Yadav', 'Ashok Yadav', 'Kiran Yadav', '1212 O, Panchsheel Park, Delhi', '110017', '9876543224'),
(16, '11th', 'Aarti Sharma', 'Vikram Sharma', 'Suman Sharma', '1313 P, Jawahar Nagar, Chennai', '600082', '9876543225'),
(17, '12th', 'Amitabh Chauhan', 'Harish Chauhan', 'Poonam Chauhan', '1414 Q, Saket, Delhi', '110017', '9876543226'),
(18, '12th', 'Priti Rani', 'Raj Kumar', 'Sunita Rani', '1515 R, Ashoka Road, Bangalore', '560025', '9876543227'),
(19, '10th', 'Nitin Kapoor', 'Sanjeev Kapoor', 'Pooja Kapoor', '1616 S, Civil Lines, Kanpur', '208001', '9876543228'),
(20, '10th', 'Roshni Patel', 'Mohan Patel', 'Sushma Patel', '1717 T, Anand Vihar, Delhi', '110092', '9876543229'),
(21, '11th', 'Aakash Joshi', 'Ravi Joshi', 'Rita Joshi', '1821 U, Hari Nagar, Delhi', '110064', '9876543230'),
(22, '11th', 'Sonali Saini', 'Rajeev Saini', 'Meenal Saini', '1922 V, Darya Ganj, Delhi', '110002', '9876543231'),
(23, '12th', 'Vikram Reddy', 'Raj Reddy', 'Kavya Reddy', '2023 W, Santacruz, Mumbai', '400054', '9876543232'),
(24, '12th', 'Ravi Kumar', 'Manohar Kumar', 'Rekha Kumar', '2124 X, Chappal Lane, Hyderabad', '500067', '9876543233'),
(25, '10th', 'Divya Bhardwaj', 'Sunil Bhardwaj', 'Neeta Bhardwaj', '2225 Y, Nampally, Hyderabad', '500001', '9876543234'),
(26, '10th', 'Raj Patel', 'Ratan Patel', 'Kiran Patel', '2326 Z, Falaknuma, Hyderabad', '500008', '9876543235'),
(27, '11th', 'Gaurav Sharma', 'Manoj Sharma', 'Geeta Sharma', '2427 A1, Shalimar Bagh, Delhi', '110088', '9876543236'),
(28, '11th', 'Ankita Singh', 'Ramesh Singh', 'Sita Singh', '2528 B2, Nirman Vihar, Delhi', '110092', '9876543237'),
(29, '12th', 'Anil Kumar', 'Hari Kumar', 'Sushma Kumar', '2629 C3, Sector 46, Noida', '201303', '9876543238'),
(30, '12th', 'Tanuja Reddy', 'Kiran Reddy', 'Lalitha Reddy', '2730 D4, Sector 50, Noida', '201304', '9876543239'),
(31, '10th', 'Sanjay Mehta', 'Rajiv Mehta', 'Rekha Mehta', '2831 E5, Lajpat Nagar, Delhi', '110024', '9876543240'),
(32, '10th', 'Geeta Agarwal', 'Anil Agarwal', 'Suman Agarwal', '2932 F6, Green Park, Delhi', '110016', '9876543241'),
(33, '11th', 'Rohan Jain', 'Amit Jain', 'Suman Jain', '3033 G7, Saket, Delhi', '110017', '9876543242'),
(34, '11th', 'Shilpa Kapoor', 'Rajesh Kapoor', 'Suman Kapoor', '3134 H8, Vikaspuri, Delhi', '110018', '9876543243'),
(35, '12th', 'Ravi Tiwari', 'Ramesh Tiwari', 'Sushma Tiwari', '3235 I9, Okhla, Delhi', '110020', '9876543244'),
(36, '12th', 'Deepika Singh', 'Vikram Singh', 'Neetu Singh', '3336 J1, Hauz Khas, Delhi', '110016', '9876543245'),
(37, '10th', 'Manish Joshi', 'Vikram Joshi', 'Sunita Joshi', '3437 K2, Pitampura, Delhi', '110034', '9876543246'),
(38, '10th', 'Sonia Verma', 'Raj Verma', 'Anita Verma', '3538 L3, Janakpuri, Delhi', '110058', '9876543247'),
(39, '11th', 'Pooja Yadav', 'Ramesh Yadav', 'Suman Yadav', '3639 M4, Patparganj, Delhi', '110092', '9876543248'),
(40, '11th', 'Rajesh Kumar', 'Suraj Kumar', 'Geeta Kumar', '3740 N5, Vikas Puri, Delhi', '110018', '9876543249'),
(41, '12th', 'Kavita Rani', 'Manoj Rani', 'Suman Rani', '3841 O6, Dwarka, Delhi', '110075', '9876543250'),
(42, '12th', 'Nisha Gupta', 'Rajeev Gupta', 'Nidhi Gupta', '3942 P7, Greater Noida', '201308', '9876547606')
(43, "12th", "Aryan Singh", "Arjun Prajapati", "Pihu Chaubey", "Maharua, Akbarpur, Ambedkar Nagar", "224168", "9555366649"),
(44, "11th", "Sudhanshu Mishra", "Ghanshyam Mishra", "Anamika Dubey", "Bikapur, Akbarpur", "224149", "6394525157");
