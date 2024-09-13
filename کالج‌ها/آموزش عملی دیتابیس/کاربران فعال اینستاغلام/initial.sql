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
-- Table structure for table `likes`
--

CREATE TABLE `likes` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `post_id` int(11) NOT NULL,
  `created_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `likes`
--

INSERT INTO `likes` (`id`, `user_id`, `post_id`, `created_at`) VALUES
(1, 25, 17, '2021-10-14 10:32:21'),
(2, 5, 2, '2021-10-26 08:47:26'),
(3, 4, 11, '2021-11-13 09:26:18'),
(4, 13, 3, '2021-11-23 22:54:16'),
(5, 21, 13, '2021-09-28 00:41:43'),
(6, 21, 12, '2021-09-25 19:08:18'),
(7, 13, 24, '2021-11-17 22:05:53'),
(8, 25, 11, '2021-09-10 18:59:49'),
(9, 8, 1, '2021-10-27 10:37:13'),
(10, 3, 3, '2021-09-02 06:41:31'),
(11, 10, 14, '2021-09-26 14:51:47'),
(12, 2, 18, '2021-11-01 22:39:03'),
(13, 7, 11, '2021-10-07 09:00:29'),
(14, 12, 18, '2021-10-19 07:48:01'),
(15, 16, 23, '2021-09-18 20:11:07'),
(16, 11, 1, '2021-09-14 09:58:13'),
(17, 1, 23, '2021-11-22 04:27:32'),
(18, 7, 5, '2021-11-12 18:27:06'),
(19, 15, 22, '2021-11-19 22:51:59'),
(20, 25, 20, '2021-10-05 06:53:02'),
(21, 20, 23, '2021-10-25 19:03:47'),
(22, 24, 20, '2021-09-22 11:48:41'),
(23, 16, 7, '2021-09-15 08:06:18'),
(24, 4, 5, '2021-11-02 06:08:46'),
(25, 6, 11, '2021-10-02 21:19:10');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `full_name`, `email`) VALUES
(1, 'nelle.lesch', 'Lyric O\'Kon', 'izboncak@yahoo.com'),
(2, 'francis.hane', 'Rod Wyman', 'ruthie08@hotmail.com'),
(3, 'kozey.marquis', 'Louie Reichert', 'fwaters@hotmail.com'),
(4, 'nolan.arnulfo', 'Isai Boehm', 'grant15@yahoo.com'),
(5, 'vcarroll', 'Chaz Schaden', 'rogahn.daryl@ryan.net'),
(6, 'mnikolaus', 'Nellie Mitchell DDS', 'mayert.gerard@adams.org'),
(7, 'jonathan59', 'Dr. Antonetta Purdy', 'ludwig89@yahoo.com'),
(8, 'johnston.seamus', 'Lenore Koelpin', 'johnpaul.bradtke@bailey.com'),
(9, 'winfield31', 'Mr. Johnathon Gulgowski', 'xjenkins@kuvalis.com'),
(10, 'oren.breitenberg', 'Zena Conn', 'herbert.ritchie@schumm.com'),
(11, 'spagac', 'Joshuah Bashirian', 'abernathy.moises@mckenzie.org'),
(12, 'rippin.zoey', 'Miss Darby Hilpert', 'wnader@gmail.com'),
(13, 'hazle29', 'Dr. Kendall Heaney II', 'florencio.watsica@dickens.com'),
(14, 'reynolds.kacey', 'Dr. Trystan Harber Sr.', 'cdaniel@hotmail.com'),
(15, 'stevie53', 'Derek Nolan', 'taufderhar@pacocha.com'),
(16, 'vmurray', 'Hailey Jones', 'hoeger.sibyl@yahoo.com'),
(17, 'xrath', 'Ms. Minerva Blanda DDS', 'jordy05@kunze.com'),
(18, 'glover.dorcas', 'Amanda Rau', 'kylee73@paucek.info'),
(19, 'kuhn.torrance', 'Santino Altenwerth', 'kbreitenberg@rolfson.com'),
(20, 'hilpert.alexander', 'Frederique Rowe', 'hermiston.keira@strosin.org'),
(21, 'trudie10', 'Geo Schimmel', 'fshields@bednar.biz'),
(22, 'halle.moore', 'Amparo Vandervort', 'wbernhard@yahoo.com'),
(23, 'blake60', 'Arthur Hartmann', 'shanahan.neva@yahoo.com'),
(24, 'beatty.keyon', 'Kaylah Kuphal', 'arvilla.schuster@yahoo.com'),
(25, 'cartwright.mackenzie', 'Dejuan O\'Connell', 'sunny.mckenzie@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `likes`
--
ALTER TABLE `likes`
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
-- AUTO_INCREMENT for table `likes`
--
ALTER TABLE `likes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
