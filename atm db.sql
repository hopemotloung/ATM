create schema atm;
create table users(
id int(2) primary key not null auto_increment,
email varchar(50) not null,
pass varchar(50) not null,
full_name varchar(50),
Balance varchar(10)
);

create table statement(
email varchar(50) not null,
dates varchar(50),
typez varchar(50),
amount varchar(50)
);

