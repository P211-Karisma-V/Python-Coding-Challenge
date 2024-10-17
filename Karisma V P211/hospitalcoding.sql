create database hospitalmanagementdb;
use hospitalmanagementdb;
---creation of table:

-- Creating Patient table
CREATE TABLE Patient (
    patientId INT PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    dateOfBirth DATE,
    gender VARCHAR(10),
    contactNumber VARCHAR(15),
    address VARCHAR(255)
);

-- Creating Doctor table
CREATE TABLE Doctor (
    doctorId INT PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    specialization VARCHAR(50),
    contactNumber VARCHAR(15)
);

-- Creating Appointment table
CREATE TABLE Appointment (
    appointmentId INT PRIMARY KEY,
    patientId INT,
    doctorId INT,
    appointmentDate DATE,
    description VARCHAR(255),
    FOREIGN KEY (patientId) REFERENCES Patient(patientId),
    FOREIGN KEY (doctorId) REFERENCES Doctor(doctorId)
);

-- Inserting values into Patient table
INSERT INTO Patient (patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address) VALUES
(1, 'Karisma', 'Vetri', '2001-05-12', 'Female', '9597478539', 'Big Street'),
(2, 'Malathi', 'VP', '2001-07-19', 'Female', '9987654321', 'New Street'),
(3, 'Shadhika', 'Doc', '2001-01-25', 'Female', '8220447201', 'Valluvar Street'),
(4, 'Harshini', 'RY', '1999-11-30', 'Female', '9943778539', 'Thiruvalluvar Street'),
(5, 'Bavanesh', 'RT', '1992-08-16', 'Male', '9876543219', 'Metu Street'),
(6, 'Uma', 'MY', '1980-03-22', 'Female', '8976543239', 'Mint Street'),
(7, 'Shobana', 'Venu', '1985-12-11', 'Female', '7891234567', 'Park Street'),
(8, 'Devi', 'Shree', '2001-06-09', 'Female', '8796543234', 'Govind Street'),
(9, 'Rama', 'chandran', '1993-04-03', 'Male', '7895678945', 'Court Street'),
(10, 'Vetri', 'velan', '1989-09-05', 'Male', '8678954398', 'God Street');

-- Inserting values into Doctor table
INSERT INTO Doctor (doctorId, firstName, lastName, specialization, contactNumber) VALUES
(1, 'Monisha', 'Murali', 'Infectious Disease', '9946789345'),
(2, 'Selvi', 'Radhakrishnan', 'Trauma Surgery', '7845364364'),
(3, 'Kaveri', 'Swaminathan', 'Spine Surgery', '8324324321'),
(4, 'Shanthi', 'williams', 'Vascular Surgery', '7897897890'),
(5, 'Swaminathan', 'Anantharaman', 'Neonatal Surgery', '9564564567');

-- Inserting values into Appointment table
INSERT INTO Appointment (appointmentId, patientId, doctorId, appointmentDate, description) VALUES
(1,1, 1, '2024-10-11', 'Consultation for infectious disease'),
(2,2, 2, '2024-10-12', 'Trauma surgery follow-up'),
(3,3, 3, '2024-10-13', 'Spine surgery consultation'),
(4,4, 4, '2024-10-14', 'Vascular surgery evaluation'),
(5,5, 5, '2024-10-15', 'Neonatal surgery follow-up'),
(6,6, 1, '2024-10-16', 'Infectious disease checkup'),
(7,7, 2, '2024-10-17', 'Trauma surgery post-op'),
(8,8, 3, '2024-10-18', 'Spinal surgery follow-up'),
(9,9, 4, '2024-10-19', 'Vascular checkup consultation'),
(10,10, 5, '2024-10-20', 'Neonatal surgery assessment');
SELECT*FROM Patient;
SELECT*FROM Doctor;
SELECT*FROM Appointment;
