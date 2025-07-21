-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 25, 2021 at 10:02 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quera`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `name`) VALUES
(21885267, 'Isabel Koss'),
(26188683, 'Prof. Bell Cremin MD'),
(57453780, 'Dr. Deondre Klein DVM'),
(63785907, 'Mikel Boyer'),
(70829981, 'Georgiana Becker II'),
(71071675, 'Miss Dovie Moen I'),
(82918742, 'Dr. Richmond Witting'),
(83531342, 'Aryanna Kunde'),
(90990159, 'Ms. Sophia Abshire'),
(98926164, 'Mario Koch');

-- --------------------------------------------------------

--
-- Table structure for table `student_courses`
--

CREATE TABLE `student_courses` (
  `id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student_courses`
--

INSERT INTO `student_courses` (`id`, `student_id`, `course_id`) VALUES
(1, 21885267, 4),
(2, 21885267, 8),
(3, 21885267, 7),
(4, 21885267, 9),
(5, 21885267, 4),
(6, 21885267, 3),
(7, 21885267, 7),
(8, 21885267, 7),
(9, 21885267, 8),
(10, 21885267, 1),
(11, 57453780, 5),
(12, 57453780, 3),
(13, 57453780, 1),
(14, 83531342, 1),
(15, 83531342, 4),
(16, 83531342, 4),
(17, 83531342, 6),
(18, 83531342, 2),
(19, 83531342, 9),
(20, 83531342, 4),
(21, 90990159, 5),
(22, 90990159, 8),
(23, 90990159, 9),
(24, 90990159, 3),
(25, 90990159, 10),
(26, 90990159, 9),
(27, 90990159, 1),
(28, 90990159, 3),
(29, 82918742, 9),
(30, 82918742, 8),
(31, 82918742, 9),
(32, 98926164, 1),
(33, 98926164, 2),
(34, 98926164, 4),
(35, 98926164, 10),
(36, 26188683, 5),
(37, 26188683, 10),
(38, 26188683, 7),
(39, 26188683, 9),
(40, 26188683, 1),
(41, 26188683, 4),
(42, 26188683, 1),
(43, 63785907, 1),
(44, 63785907, 10),
(45, 63785907, 2),
(46, 63785907, 10),
(47, 63785907, 7),
(48, 63785907, 8),
(49, 63785907, 4),
(50, 70829981, 10),
(51, 70829981, 4),
(52, 70829981, 9),
(53, 71071675, 9),
(54, 71071675, 5),
(55, 71071675, 4),
(56, 71071675, 3),
(57, 71071675, 5),
(58, 71071675, 6),
(59, 71071675, 9),
(60, 71071675, 8),
(61, 71071675, 10),
(62, 71071675, 8);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student_courses`
--
ALTER TABLE `student_courses`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=98926165;

--
-- AUTO_INCREMENT for table `student_courses`
--
ALTER TABLE `student_courses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
