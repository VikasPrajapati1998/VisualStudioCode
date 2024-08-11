show databases;
use mydatabase;
show tables;
select * from sellers;
create table customer_sellers(
id int auto_increment primary key,
name varchar(255), 
address varchar(255));

INSERT INTO customer_sellers (name, address) VALUES
('Emily Davis', '123 Maple Street, Springfield, IL'),
('Michael Johnson', '456 Oak Avenue, Springfield, IL'),
('Sophia Williams', '789 Pine Road, Springfield, IL'),
('James Brown', '101 Elm Lane, Springfield, IL'),
('Olivia Martinez', '202 Cedar Street, Springfield, IL'),
('Liam Anderson', '303 Birch Avenue, Springfield, IL'),
('Emma Thomas', '404 Walnut Road, Springfield, IL'),
('Noah White', '505 Cherry Lane, Springfield, IL'),
('Ava Harris', '606 Ash Street, Springfield, IL'),
('Lucas Clark', '707 Elm Avenue, Springfield, IL'),
('Mia Lewis', '808 Oak Lane, Springfield, IL'),
('Ethan Robinson', '909 Pine Street, Springfield, IL'),
('Isabella Walker', '1010 Maple Avenue, Springfield, IL'),
('Alexander Hall', '1111 Birch Lane, Springfield, IL'),
('Charlotte Allen', '1212 Cedar Road, Springfield, IL'),
('Benjamin Young', '1313 Walnut Avenue, Springfield, IL'),
('Amelia King', '1414 Cherry Street, Springfield, IL'),
('William Scott', '1515 Ash Lane, Springfield, IL'),
('Harper Adams', '1616 Elm Street, Springfield, IL'),
('Daniel Mitchell', '1717 Oak Road, Springfield, IL');
