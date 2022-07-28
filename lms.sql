-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 06, 2020 at 02:34 PM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

CREATE DATABASE LMS;
USE LMS;
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--


CREATE TABLE books (
  b_id INT NOT NULL AUTO_INCREMENT,
  b_name char(60) DEFAULT NULL,
  author char(50) DEFAULT NULL,
  sub char(50) DEFAULT NULL,
  total INT DEFAULT NULL,
  PRIMARY KEY (b_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `books`
--

INSERT INTO books (b_id, b_name, author, sub, total) VALUES
(1, 'learn python', 'ahmad', 'technology', 1),
(2, 'data Analytics with python', 'alex', 'technology', 2),
(3, 'data science with python', 'yusuf', 'technology', 3),
(4, 'machine learning With Python', 'joko', 'technology', 2),
(5, 'business intellegence', 'syamsul', 'technology', 1),
(6, 'affinity designer', 'hensa', 'design', 1);

-- --------------------------------------------------------

--
-- Table structure for table `member`
--


CREATE TABLE members (
  m_id INT NOT NULL AUTO_INCREMENT,
  m_name char(30) DEFAULT NULL,
  phone char(15) DEFAULT NULL,
  email char(60) DEFAULT NULL,
  address char(100) DEFAULT NULL,
  PRIMARY KEY (m_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `member`
--

INSERT INTO members (m_id, m_name, phone, email, address) VALUES
(1, 'adnan', '987177171', 'rakesh@cbsetoday.com', 'cf-4 brij vihar'),
(2, 'siregar', '2345677890', 'sam@gmail.com', 'f-124 surya nagar'),
(3, 'andrew', '987383843', 'kamal@mail.com', 'cf-9 brij vihar'),
(4, 'umar', '65775575', 'rakshit@gmail.com', 'f-32 surya nagar');

-- --------------------------------------------------------

--
-- Table structure for table `loans`
--


CREATE TABLE loans (
  regno INT NOT NULL AUTO_INCREMENT,
  b_id INT NOT NULL,
  b_name char(60) DEFAULT NULL,
  m_id INT NOT NULL,
  m_name char(30) DEFAULT NULL,
  l_date date DEFAULT NULL,
  r_date date DEFAULT NULL,
  PRIMARY KEY (regno)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE loans
ADD FOREIGN KEY(b_id)
REFERENCES books(b_id);

ALTER TABLE loans
ADD FOREIGN KEY(m_id)
REFERENCES members(m_id);

--
-- Dumping data for table `loans`
--

INSERT INTO loans (regno, b_id, b_name, m_id, m_name, l_date, r_date) VALUES
(1, 6, 'affinity designer', 4, 'umar', '2022-10-06', '2022-12-06'),
(2, 2, 'data Analytics with python', 1, 'adnan', '2022-10-06', '2022-12-06'),
(3, 2, 'data Analytics with python', 3, 'andrew', '2022-10-06', '2022-12-06'),
(4, 5, 'business intellegence', 1, 'adnan', '2022-10-06', '2022-12-06');

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
