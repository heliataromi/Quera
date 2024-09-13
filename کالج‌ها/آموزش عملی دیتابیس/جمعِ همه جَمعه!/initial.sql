-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 25, 2021 at 12:06 PM
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
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `job_id` int(11) NOT NULL,
  `squad_id` int(11) NOT NULL,
  `salary` decimal(15,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`id`, `name`, `job_id`, `squad_id`, `salary`) VALUES
(1, 'Carole Wolff', 19, 7, '6423229.00'),
(2, 'Santiago Kshlerin', 16, 4, '2039990.00'),
(3, 'Braden Parker', 6, 12, '89905926.00'),
(4, 'Dr. Francesca Medhurst', 11, 6, '1193498.00'),
(5, 'Catharine Volkman', 7, 1, '946360005.00'),
(6, 'Miss Chaya Renner', 14, 18, '431927610.00'),
(7, 'Hudson Lubowitz', 8, 13, '83148.00'),
(8, 'Janiya Bayer', 9, 14, '343093.00'),
(9, 'Dr. Tamara Bogan V', 10, 16, '34101651.00'),
(10, 'Delores Hickle', 3, 13, '4987188.00'),
(11, 'Jaquan Rodriguez', 4, 13, '1883308.00'),
(12, 'Clemmie Kuhn', 15, 10, '574409.00'),
(13, 'Prof. Antwan McKenzie', 12, 4, '96293839.00'),
(14, 'Teresa King', 14, 8, '704389.00'),
(15, 'Gillian Grimes', 10, 9, '3644715.00'),
(16, 'Prof. Rylan Jenkins I', 13, 11, '343639752.00'),
(17, 'Kiara Bailey', 16, 11, '31941.00'),
(18, 'Otha Lockman', 5, 8, '875226494.00'),
(19, 'Dr. Kevon Schiller DDS', 19, 17, '234801.00'),
(20, 'Liza Satterfield', 19, 5, '33414441.00'),
(21, 'Kaya Labadie', 13, 15, '44694906.00'),
(22, 'Oran Macejkovic', 12, 18, '781722190.00'),
(23, 'Elisabeth Lehner PhD', 3, 1, '835399274.00'),
(24, 'Aric Daniel', 12, 7, '913205.00'),
(25, 'Marcelino Emard', 7, 6, '93434977.00'),
(26, 'Donavon Jenkins', 4, 19, '25974941.00'),
(27, 'Dakota Orn', 9, 16, '422611643.00'),
(28, 'Hannah Green', 16, 5, '9512436.00'),
(29, 'Evie Sipes DVM', 6, 3, '12553780.00'),
(30, 'Flossie Stehr', 20, 11, '8926635.00'),
(31, 'Keyon Pacocha', 3, 17, '609524189.00'),
(32, 'Isaias Wilkinson', 11, 14, '846279598.00'),
(33, 'Ms. Elissa Lowe', 11, 15, '146380.00'),
(34, 'Frida Buckridge', 20, 8, '19991410.00'),
(35, 'Ms. Aryanna Hayes Jr.', 12, 18, '950293.00'),
(36, 'Faustino Gislason', 16, 20, '805522.00'),
(37, 'Heather Howell', 16, 18, '57499.00'),
(38, 'Jada Corkery', 20, 8, '5169171.00'),
(39, 'Kenton Reichel', 8, 14, '49024.00'),
(40, 'Queenie Wolff', 17, 12, '936908.00'),
(41, 'Prof. Haskell Padberg Jr.', 18, 3, '10260912.00'),
(42, 'Ms. Yazmin Marks', 6, 19, '753452155.00'),
(43, 'Baron Nienow', 1, 17, '79279065.00'),
(44, 'Skylar Metz', 18, 12, '9255179.00'),
(45, 'Noemie Mertz', 13, 6, '11872.00'),
(46, 'Laurine Fadel MD', 20, 1, '142243340.00'),
(47, 'Morgan Satterfield', 10, 7, '67396.00'),
(48, 'Mrs. Ethyl Reichel', 4, 15, '658121037.00'),
(49, 'Estefania Jaskolski', 15, 3, '469201.00'),
(50, 'Ana Lebsack', 19, 9, '941398858.00'),
(51, 'Mr. Sherman Casper', 4, 13, '5193934.00'),
(52, 'Lulu Ward', 16, 10, '70381913.00'),
(53, 'Filiberto Boyer DDS', 19, 7, '407768496.00'),
(54, 'Lilla Dickinson', 1, 5, '73424.00'),
(55, 'Evelyn Hauck', 13, 11, '6232286.00'),
(56, 'Mr. Javonte Beer', 15, 6, '833873.00'),
(57, 'Noel Schiller', 6, 12, '23024983.00'),
(58, 'Kole Bernier Sr.', 14, 2, '6272239.00'),
(59, 'Glenna Rempel', 5, 11, '877572.00'),
(60, 'Tillman Volkman', 3, 19, '25122.00'),
(61, 'Osvaldo Reynolds', 15, 9, '839843.00'),
(62, 'Prof. Benedict Jones MD', 12, 9, '651213.00'),
(63, 'Arvilla Schneider', 4, 19, '55709121.00'),
(64, 'Miss Valentina Wunsch Sr.', 14, 7, '851019.00'),
(65, 'Mr. Fausto Maggio', 12, 13, '554238994.00'),
(66, 'Burley Cremin', 11, 14, '87046.00'),
(67, 'Trever Bosco', 18, 14, '87992.00'),
(68, 'Aylin Collins', 2, 10, '54279.00'),
(69, 'Joanny Price', 18, 11, '41043.00'),
(70, 'Dr. Eula Parker', 15, 20, '40083296.00'),
(71, 'Kailyn Padberg PhD', 1, 16, '337211411.00'),
(72, 'Germaine Legros', 14, 9, '36755.00'),
(73, 'Lucio Zulauf', 3, 2, '14647927.00'),
(74, 'Wava VonRueden', 14, 16, '14348285.00'),
(75, 'Billy Wisozk', 14, 20, '981590351.00'),
(76, 'Abbigail Altenwerth', 6, 5, '97527.00'),
(77, 'Moriah Wilderman', 7, 13, '38887.00'),
(78, 'Tomas Muller', 7, 17, '75648.00'),
(79, 'Dr. Meghan Bechtelar', 17, 16, '837593.00'),
(80, 'Prof. Royal Kutch III', 1, 14, '82236.00'),
(81, 'Hillard Schowalter', 12, 2, '39804445.00'),
(82, 'Lavinia Dibbert', 3, 3, '397543.00'),
(83, 'Orlo Gerlach', 16, 12, '33889657.00'),
(84, 'Ahmad Waters', 7, 16, '44346726.00'),
(85, 'Cecil Lueilwitz IV', 1, 20, '390863.00'),
(86, 'Amaya Corkery IV', 8, 5, '868098.00'),
(87, 'Jedediah O\'Reilly', 4, 9, '58795.00'),
(88, 'Vicky Koch', 12, 5, '511267.00'),
(89, 'Jonathan Rolfson I', 16, 2, '557626589.00'),
(90, 'Ron Braun', 15, 12, '2560623.00'),
(91, 'Renee Zemlak', 18, 16, '625826622.00'),
(92, 'Prof. Marina Blick', 2, 16, '60481715.00'),
(93, 'Prof. Ansel Franecki IV', 5, 13, '7187172.00'),
(94, 'Karolann Fisher', 3, 20, '7024853.00'),
(95, 'Minnie Davis', 12, 9, '229107584.00'),
(96, 'Ms. Caroline Hegmann', 1, 5, '2824980.00'),
(97, 'Mose Kemmer', 5, 13, '436499.00'),
(98, 'Angelina Douglas I', 7, 15, '549976445.00'),
(99, 'Jarvis Wilkinson', 18, 8, '98005.00'),
(100, 'Jacquelyn Bruen', 6, 10, '42566.00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
