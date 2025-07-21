-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 25, 2021 at 02:27 PM
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
-- Table structure for table `carts`
--

CREATE TABLE `carts` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `items` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `carts`
--

INSERT INTO `carts` (`id`, `user_id`, `items`) VALUES
(1, 3, '[10374,10798,7407,13660]'),
(2, 3, '[13648]'),
(3, 3, '[16215,6941,15879,11249,8771]'),
(4, 3, '[12468,13079,7662,7809]'),
(5, 4, '[10126,13234,15344,14079]'),
(6, 4, '[16145]'),
(7, 4, '[11925]'),
(8, 4, '[9261,10658,16306]'),
(9, 5, '[10647,14443,10692,9865,7580]'),
(10, 5, '[11672,8092,10226,7995,11313]'),
(11, 5, '[10660,8864,7141]'),
(12, 10, '[16162,11015]'),
(13, 10, '[13541]'),
(14, 17, '[9194]'),
(15, 32, '[12562,9994,9816,7269]'),
(16, 32, '[8893]'),
(17, 32, '[9212,8295,14240]'),
(18, 36, '[11258,9108,12034,13056,9179]'),
(19, 36, '[15557,10838]'),
(20, 36, '[9436,13348,13257,9876]'),
(21, 46, '[16089,15525,13669,8596,13318]');

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `id` int(11) NOT NULL,
  `cart_id` int(11) NOT NULL,
  `track_id` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`id`, `cart_id`, `track_id`) VALUES
(1, 6, 'galolUrVccipsnJcTISHMbykauDzovmuFFhIONLHMekvvbZiayFKmCltDpezDnEE'),
(2, 7, 'XCbpnrWhhDyzoZWSLsDyVtQOcUlmLXpSnhxjnJWvAArjPctIgZjsKKIJBTKrwccF'),
(3, 12, 'ZOCCmTKPRuUuoSRAWWtsJxISabdticbpXuMoYIUiNsIhiJCmzStVxZfJVKhqMRCu'),
(4, 16, 'eWdisnCUqQgnpvanCsOSvZeWuzmMkRHngjxsomvmlpnKHcmUdYmVfihCeTGZovtf'),
(5, 20, 'UrtdGamHWpXGdTshnTaLmYUOybgWPqHGfeFtXsSoZAetGrdMfLeVmlfbMTMQQeYz'),
(6, 21, 'BukMguWUJndtIWePDNyHjYRtGIVdeKnARqpKJSmqWmStIaVJNodRGztiVwIvPFlb');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `password`) VALUES
(1, 'emma22@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(2, 'allie72@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(3, 'awintheiser@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(4, 'zbreitenberg@example.net', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(5, 'feest.katelynn@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(6, 'will.thea@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(7, 'awalter@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(8, 'alanna63@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(9, 'zelda.nienow@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(10, 'annabell.metz@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(11, 'zfriesen@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(12, 'champlin.muhammad@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(13, 'francisco.koepp@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(14, 'pagac.fannie@example.net', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(15, 'sanford.lucy@example.net', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(16, 'reese82@example.net', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(17, 'kris.callie@example.net', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(18, 'cora73@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(19, 'uhowe@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(20, 'ngleason@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(21, 'zaria78@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(22, 'cordia.aufderhar@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(23, 'haley.schuppe@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(24, 'wuckert.zoie@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(25, 'wyman.dayna@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(26, 'lnienow@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(27, 'horace.huels@example.net', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(28, 'gutkowski.larue@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(29, 'miles.bayer@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(30, 'terrence71@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(31, 'morar.grover@example.net', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(32, 'hackett.rebecca@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(33, 'alvah.kovacek@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(34, 'raleigh32@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(35, 'emmett75@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(36, 'nitzsche.vivien@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(37, 'trunolfsson@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(38, 'okeefe.kellie@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(39, 'eluettgen@example.net', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(40, 'agoodwin@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(41, 'percy52@example.net', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(42, 'rtowne@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(43, 'torp.brenden@example.net', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(44, 'kirlin.gavin@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(45, 'felipe20@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(46, 'micah.goldner@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(47, 'cjakubowski@example.net', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(48, 'yschmidt@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(49, 'hoeger.ahmad@example.com', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK'),
(50, 'adella33@example.org', '$2y$10$DplBcqgazU3PriJFn0373ur8pSXmwIYEqflCJesnp5stXNHL9A/lK');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `carts`
--
ALTER TABLE `carts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `carts`
--
ALTER TABLE `carts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
