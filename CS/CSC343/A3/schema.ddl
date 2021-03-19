-- The constraints from the domain could not be enforced:
-- no.

-- What constraints that could have been enforced were not enforced? why not?
-- 1.the number of customers of one reservation is bigger than the capacity of the corresponding car.
-- 2.A customer can change a confirmed reservation (only once).
-- Since we can use triggers or assertions to complete them. But in this assignment, we can not use triggers or assertions.
drop schema if exists carschema cascade;
create schema carschema;
set search_path to carschema;

-- a customer who envolved in car renting
CREATE TABLE Customer (
-- the name os the customer
Name TEXT NOT NULL,
-- the age of the customer
Age INT NOT NULL,
-- the email address of the customer
Email TEXT PRIMARY KEY),
check (Age > 0));

-- a model that was rent in the company business opreation
CREATE TABLE Model (
ID INT PRIMARY KEY,
-- the name of the model
Name TEXT NOT NULL,
-- the type of the model
Vehicle_Type TEXT NOT NULL,
-- the number of the model
Model_Number INT NOT NULL,
-- the capacity of the model
Capacity INT NOT NULL,
check (Capacity > 0));

-- a Rentalstation is a location where car was picked up and sent back
CREATE TABLE Rentalstation (
-- the code for the station
Station_Code INT PRIMARY KEY,
-- the name for the station
Name TEXT NOT NULL,
-- the address for the station
Address TEXT NOT NULL,
-- the area code for the station
Area_Code TEXT NOT NULL,
-- the city for the station
City TEXT NOT NULL);

-- a car
CREATE TABLE Car (
ID INT PRIMARY KEY,
-- the license_number of the car
License_Plate_Number TEXT UNIQUE NOT NULL,
-- the station code for the car
Station_Code INT NOT NULL references Rentalstation(Station_Code),
-- the model id for the car
Model_Id INT NOT NULL references Model(ID));

-- a reservation is that one or multiple customers made
CREATE TABLE Reservation (
ID INT PRIMARY KEY,
-- the from-date of the reservation
From_Date TIMESTAMP NOT NULL,
-- the to-date of the reservation
To_Date TIMESTAMP NOT NULL,
-- the corresponding car-id
Car_ID INT NOT NULL references Car(ID),
-- the previous reservation id if it exists otherwise null
Old_Reservation_ID INT references Reservation(ID),
-- the reservation status
Status TEXT NOT NULL check (Status = 'Confirmed' or Status = 'Ongoing' or
Status = 'Completed' or Status = 'Cancelled'));

-- a customer reservation is where customer made a specific reservation, such as cutomer A made a reservation with id 1
CREATE TABLE Customer_reservation (
-- the customer email
Customer_Email TEXT NOT NULL references Customer(Email),
-- the reservation id that the customer made
Reservation_ID INT references Reservation(ID));
