create database if not exists ride_share_hub_db;

USE ride_share_hub_db;

create table users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

create table contact_us (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255),
    email_address VARCHAR(255),
    phone_no VARCHAR(20),
    subject VARCHAR(255),
    message TEXT
);

create table register (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    mobile VARCHAR(15) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    address TEXT NOT NULL
);


select * from users;
select * from contact_us;
select * from register;

SET SQL_SAFE_UPDATES = 0;

