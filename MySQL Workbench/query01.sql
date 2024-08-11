use arjundb;
Create table Persons (
	PersonID int,
    FirstName varchar(255),
    LastName varchar(255),
    Address varchar(255),
    City varchar(255)
);

Create table Employee as
	select PersonID as EmployeeID,
    FirstName, LastName, Address, City from Persons;

show tables;
