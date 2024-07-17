create database SchoolSystem;
use schoolsystem;

create table school (emis_code int(20) primary key not null,school_name varchar(100),School_Shift varchar(30), school_level varchar(30),Establishment_year int (20), School_medium varchar(30), Total_students int(20),Total_Teachers int(20));

create table Union_council(uc_number int (30) primary key not null, uc_name varchar(30));

create table contact_info (contact_info_id int (30) primary key NOT NULL, district varchar (30), city varchar(30), tehsil varchar(30),emis_code int (20), markaz varchar(30),moza varchar(30),street_name varchar(30) , uc_number int(30),foreign key (uc_number) references union_council(uc_number), foreign key (emis_code) references school(emis_code));

create table head (head_id int(20) primary key not null, head_name varchar(50), head_type varchar(50), head_grade int (10), emis_code int(20), foreign key (emis_code) references school(emis_code));

create table building (building_id int (50) primary key not null, covered_area int (50), uncovered_area int (50), Total_area int (50),internet int (50),caregivers int (50),playground int (50), classes int (50),total_computers int (50),ece_rooms int (50), total_rooms int (50),emis_code int (20), foreign key (emis_code) references school(emis_code));

create table game (game_id int(20) primary key not null, game_name varchar(30));

create table lab (lab_id int(30) primary key not null, lab_name varchar(50));

CREATE TABLE building_lab (building_id INT(50) NOT NULL,lab_id INT(30) NOT NULL,PRIMARY KEY (building_id, lab_id),FOREIGN KEY (building_id) REFERENCES building(building_id), foreign key (lab_id) references lab(lab_id));

create table gameschool (emis_code int(20) not null, game_id int(20) not null, foreign key (emis_code) references school(emis_code),foreign key(game_id) references game(game_id), primary key (emis_code,game_id));