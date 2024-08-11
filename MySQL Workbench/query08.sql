show databases;
use arjundb;
CREATE TABLE student(
	roll INT PRIMARY KEY,
    class VARCHAR(50),
    name VARCHAR(255),
    fatherName VARCHAR(255),
    motherName VARCHAR(255),
    address VARCHAR(255),
    pin VARCHAR(10),
    mobileNumber VARCHAR(15)
);

INSERT INTO student (roll, class, name, fatherName, motherName, address, pin, mobileNumber) VALUES
(1, '10th', 'John Doe', 'Robert Doe', 'Jane Doe', '123 Elm Street, Springfield', '62701', '555-1234'),
(2, '10th', 'Jane Smith', 'Michael Smith', 'Emily Smith', '456 Oak Avenue, Springfield', '62702', '555-5678'),
(3, '11th', 'Alice Johnson', 'David Johnson', 'Laura Johnson', '789 Pine Road, Springfield', '62703', '555-9101'),
(4, '11th', 'Bob Brown', 'John Brown', 'Sara Brown', '101 Maple Lane, Springfield', '62704', '555-1122'),
(5, '12th', 'Charlie Davis', 'Richard Davis', 'Nancy Davis', '202 Birch Street, Springfield', '62705', '555-3344'),
(6, '12th', 'Diana Evans', 'George Evans', 'Lisa Evans', '303 Cedar Road, Springfield', '62706', '555-5566'),
(7, '10th', 'Eric Wilson', 'James Wilson', 'Angela Wilson', '404 Walnut Avenue, Springfield', '62707', '555-7788'),
(8, '10th', 'Fiona Clark', 'Edward Clark', 'Rachel Clark', '505 Cherry Lane, Springfield', '62708', '555-9900'),
(9, '11th', 'George Martinez', 'William Martinez', 'Hannah Martinez', '606 Ash Street, Springfield', '62709', '555-1234'),
(10, '11th', 'Hannah Lee', 'Christopher Lee', 'Linda Lee', '707 Elm Street, Springfield', '62710', '555-5678'),
(11, '12th', 'Ian White', 'Daniel White', 'Barbara White', '808 Oak Avenue, Springfield', '62711', '555-9101'),
(12, '12th', 'Judy Adams', 'Mark Adams', 'Susan Adams', '909 Pine Road, Springfield', '62712', '555-1122'),
(13, '10th', 'Kevin Miller', 'Paul Miller', 'Deborah Miller', '1010 Maple Lane, Springfield', '62713', '555-3344'),
(14, '10th', 'Laura Thompson', 'Steven Thompson', 'Nancy Thompson', '1111 Birch Street, Springfield', '62714', '555-5566'),
(15, '11th', 'Mike Roberts', 'Andrew Roberts', 'Catherine Roberts', '1212 Cedar Road, Springfield', '62715', '555-7788'),
(16, '11th', 'Nina Harris', 'Gary Harris', 'Sandra Harris', '1313 Walnut Avenue, Springfield', '62716', '555-9900'),
(17, '12th', 'Oliver Scott', 'Eric Scott', 'Linda Scott', '1414 Cherry Lane, Springfield', '62717', '555-1234'),
(18, '12th', 'Pamela Green', 'Anthony Green', 'Jessica Green', '1515 Ash Street, Springfield', '62718', '555-5678'),
(19, '10th', 'Quincy Young', 'Eugene Young', 'Helen Young', '1616 Elm Street, Springfield', '62719', '555-9101'),
(20, '10th', 'Rachel Baker', 'Albert Baker', 'Nancy Baker', '1717 Oak Avenue, Springfield', '62720', '555-1122'),
(21, '11th', 'Steve Carter', 'John Carter', 'Martha Carter', '1821 Pine Road, Springfield', '62721', '555-3344'),
(22, '11th', 'Tina Foster', 'Charles Foster', 'Diana Foster', '1922 Maple Lane, Springfield', '62722', '555-5566'),
(23, '12th', 'Ulysses Grant', 'Harold Grant', 'Karen Grant', '2023 Birch Street, Springfield', '62723', '555-7788'),
(24, '12th', 'Vera Smith', 'Walter Smith', 'Grace Smith', '2124 Cedar Road, Springfield', '62724', '555-9900'),
(25, '10th', 'Walter Jones', 'Thomas Jones', 'Helen Jones', '2225 Walnut Avenue, Springfield', '62725', '555-1234'),
(26, '10th', 'Xena Black', 'Frank Black', 'Eleanor Black', '2326 Cherry Lane, Springfield', '62726', '555-5678'),
(27, '11th', 'Yvonne Brooks', 'Steven Brooks', 'Anna Brooks', '2427 Ash Street, Springfield', '62727', '555-9101'),
(28, '11th', 'Zane Adams', 'Jeffrey Adams', 'Karen Adams', '2528 Elm Street, Springfield', '62728', '555-1122'),
(29, '12th', 'Abigail Clark', 'Paul Clark', 'Linda Clark', '2629 Oak Avenue, Springfield', '62729', '555-3344'),
(30, '12th', 'Benjamin Davis', 'Samuel Davis', 'Evelyn Davis', '2730 Pine Road, Springfield', '62730', '555-5566'),
(31, '10th', 'Catherine Evans', 'Michael Evans', 'Sarah Evans', '2831 Maple Lane, Springfield', '62731', '555-7788'),
(32, '10th', 'David Brown', 'James Brown', 'Lisa Brown', '2932 Birch Street, Springfield', '62732', '555-9900'),
(33, '11th', 'Eleanor Green', 'Andrew Green', 'Rebecca Green', '3033 Cedar Road, Springfield', '62733', '555-1234'),
(34, '11th', 'Frank Harris', 'Robert Harris', 'Jessica Harris', '3134 Walnut Avenue, Springfield', '62734', '555-5678'),
(35, '12th', 'Grace Mitchell', 'Paul Mitchell', 'Anna Mitchell', '3235 Cherry Lane, Springfield', '62735', '555-9101'),
(36, '12th', 'Henry Thompson', 'David Thompson', 'Emily Thompson', '3336 Ash Street, Springfield', '62736', '555-1122'),
(37, '10th', 'Ivy White', 'Edward White', 'Sophia White', '3437 Elm Street, Springfield', '62737', '555-3344'),
(38, '10th', 'James Scott', 'Ronald Scott', 'Grace Scott', '3538 Oak Avenue, Springfield', '62738', '555-5566'),
(39, '11th', 'Katherine Lewis', 'Thomas Lewis', 'Emma Lewis', '3639 Pine Road, Springfield', '62739', '555-7788'),
(40, '11th', 'Leo Adams', 'Daniel Adams', 'Mia Adams', '3740 Maple Lane, Springfield', '62740', '555-9900'),
(41, '12th', 'Mia Carter', 'Christopher Carter', 'Sarah Carter', '3841 Birch Street, Springfield', '62741', '555-1234'),
(42, '12th', 'Nathan Young', 'Peter Young', 'Olivia Young', '3942 Cedar Road, Springfield', '62742', '555-5678'),
(43, '10th', 'Olivia Green', 'John Green', 'Emma Green', '4043 Walnut Avenue, Springfield', '62743', '555-9101'),
(44, '10th', 'Paul Adams', 'Harry Adams', 'Sophia Adams', '4144 Cherry Lane, Springfield', '62744', '555-1122'),
(45, '11th', 'Quinn Scott', 'George Scott', 'Isabella Scott', '4245 Ash Street, Springfield', '62745', '555-3344'),
(46, '11th', 'Rachel Harris', 'Jacob Harris', 'Ava Harris', '4346 Elm Street, Springfield', '62746', '555-5566'),
(47, '12th', 'Samuel White', 'Benjamin White', 'Lily White', '4447 Oak Avenue, Springfield', '62747', '555-7788'),
(48, '12th', 'Tina Brown', 'William Brown', 'Zoe Brown', '4548 Pine Road, Springfield', '62748', '555-9900'),
(49, '10th', 'Ursula Clark', 'James Clark', 'Ella Clark', '4649 Maple Lane, Springfield', '62749', '555-1234'),
(50, '10th', 'Victor Miller', 'Samuel Miller', 'Mia Miller', '4750 Birch Street, Springfield', '62750', '555-5678');
