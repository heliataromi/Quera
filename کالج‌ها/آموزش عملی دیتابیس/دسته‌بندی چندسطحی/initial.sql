-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 26, 2021 at 09:31 AM
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
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `parent_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `title`, `slug`, `parent_id`) VALUES
(1, 'ad', 'ratione-dolorem-sed-totam-eos-aliquam', NULL),
(2, 'ut totam soluta', 'praesentium-vel-et-nobis-quisquam-quod-minima-deserunt', NULL),
(3, 'at dolorum', 'ut-et-voluptas-et-optio', NULL),
(4, 'consectetur doloribus sit', 'nulla-veritatis-est-aspernatur-est-necessitatibus-ut-iure', NULL),
(5, 'facilis qui ut', 'est-quibusdam-nisi-consequatur-rerum', NULL),
(6, 'nihil est', 'non-facilis-voluptatem-aut-voluptatem-eius-consequuntur', NULL),
(7, 'repellendus optio', 'ducimus-explicabo-a-et-rerum-dignissimos-qui', NULL),
(8, 'ab', 'nam-veniam-nulla-corporis-debitis', NULL),
(9, 'quidem minima', 'aut-vel-nisi-qui-nesciunt-necessitatibus-cumque-ut', NULL),
(10, 'illum dignissimos', 'ut-quas-vitae-ullam-aliquid-et-ea-inventore', NULL),
(11, 'hic', 'in-laborum-quo-nesciunt', NULL),
(12, 'qui ipsam', 'corrupti-harum-omnis-voluptatibus-sint-provident-itaque-dolor', NULL),
(13, 'blanditiis', 'quod-recusandae-iusto-beatae-cupiditate', NULL),
(14, 'aliquam', 'accusantium-quo-optio-unde-quidem-expedita', NULL),
(15, 'in vero sit', 'est-impedit-inventore-quos-ad', NULL),
(16, 'aut mollitia', 'iure-exercitationem-voluptatem-incidunt-incidunt-mollitia-enim', 1),
(17, 'esse et', 'iure-tempore-rerum-beatae-occaecati-occaecati-omnis-numquam', 2),
(18, 'iusto', 'suscipit-voluptates-consectetur-qui', 5),
(20, 'laborum in', 'dolorem-vel-aut-rerum-delectus-eos-nisi-ipsum', 11),
(21, 'veniam odit velit', 'porro-quo-aut-autem-quo-sequi-odio-quae-id', 3),
(22, 'culpa sed', 'numquam-aut-sed-officiis-harum-omnis-molestiae-eum-est', 15),
(23, 'consequatur', 'aliquid-ad-qui-sit-ut-voluptas', 7),
(24, 'et iure', 'optio-temporibus-veritatis-soluta-quasi', 21),
(25, 'maiores aut hic', 'asperiores-vel-quos-dolores', 21),
(26, 'accusamus necessitatibus', 'aut-placeat-fuga-occaecati-quis-voluptatum-sapiente-reiciendis', 9),
(27, 'nobis eum maxime', 'sapiente-saepe-quia-non-facilis-animi-omnis-numquam-dolor', 5),
(28, 'quisquam dolorum at', 'iste-sed-est-eveniet-consequatur-nulla-totam', 11),
(30, 'qui aut non', 'sunt-rerum-officiis-quidem-nisi-sint', 2),
(31, 'vel sint eius', 'molestiae-laborum-quos-aut-sunt', 10),
(32, 'itaque', 'voluptates-placeat-sunt-qui-natus-dicta', 6),
(33, 'consequuntur', 'repellendus-iusto-voluptatum-illum-qui-qui', 24),
(35, 'non molestiae', 'facilis-tempora-voluptatibus-non-nemo-quas-qui-enim', 23),
(36, 'corporis illo', 'omnis-quam-voluptatem-voluptatem-odio-atque-ipsum', 21),
(37, 'occaecati et', 'nemo-ab-corrupti-veritatis-dignissimos-voluptatum-ea', 31),
(39, 'rem', 'libero-excepturi-eius-a-et', 25),
(40, 'et cumque sunt', 'iure-rerum-vero-est-nostrum-aut-facere', 16),
(41, 'et non', 'doloribus-corrupti-inventore-quos-dolorem-non', 5),
(42, 'recusandae', 'sed-voluptas-totam-molestiae-animi-molestias-voluptate', 16),
(43, 'dignissimos', 'blanditiis-molestiae-asperiores-expedita-qui-tenetur-magni', 35),
(45, 'ipsa', 'ut-minus-sit-harum-quas-nihil', 10),
(46, 'autem', 'accusamus-nemo-doloremque-voluptates-corrupti-quia-aut-labore', 4),
(48, 'quia', 'id-aut-ullam-eaque-nobis-ea-qui-eum', 33),
(49, 'inventore quis', 'recusandae-et-consequuntur-vitae-quaerat-cumque-nihil', 25),
(50, 'iure', 'repudiandae-velit-sunt-quia-qui-eveniet', 32),
(51, 'accusantium dolorem et', 'modi-est-molestiae-vitae-sint-quam', 13),
(52, 'sit', 'quos-et-dicta-odio-officia-minus-aut-vel', 49),
(55, 'incidunt', 'provident-ipsum-ut-non-qui-et-ut-placeat', 8),
(56, 'odit ullam tempore', 'nihil-delectus-ut-deserunt-animi-expedita-sit', 45),
(57, 'unde', 'reprehenderit-fuga-aliquam-quia-doloremque-autem-veritatis', 3),
(58, 'ad', 'assumenda-rerum-nulla-vel-sint-pariatur-accusantium', 24),
(61, 'autem cum', 'dolores-eos-laboriosam-quia-corrupti-ipsa-suscipit', 26),
(62, 'et aut', 'quae-corrupti-enim-delectus-tenetur-optio', 42),
(66, 'minima inventore asperiores', 'excepturi-dolorem-natus-reiciendis-aspernatur-dolore-fuga-quisquam', 25),
(68, 'esse voluptatem delectus', 'mollitia-suscipit-blanditiis-asperiores-est-alias-voluptates', 27),
(69, 'facere nobis commodi', 'quos-nam-voluptatem-aspernatur-odio-itaque-incidunt-consectetur', 55),
(70, 'voluptas quibusdam', 'optio-quos-voluptas-omnis-dolorum-est-officia-velit', 18),
(72, 'recusandae', 'vero-vero-ut-nam-mollitia-possimus-sunt-et-facere', 24),
(73, 'necessitatibus sint', 'molestias-eius-dolore-voluptatem-delectus', 18),
(75, 'explicabo eum', 'consequatur-molestiae-asperiores-ipsa-commodi', 68),
(77, 'dignissimos', 'maiores-voluptatum-hic-est-autem-id-qui-est', 12),
(80, 'et', 'voluptatem-nisi-et-voluptatem-explicabo-quas', 43),
(81, 'quis quo accusamus', 'quia-sapiente-illo-ipsa-qui', 26),
(83, 'quidem aut repudiandae', 'repellat-id-atque-molestiae-qui-adipisci-asperiores', 4),
(84, 'esse quia', 'in-aut-vel-alias-sunt-natus-dolore-a-excepturi', 77),
(87, 'expedita ipsa itaque', 'quo-provident-enim-dolores-et-necessitatibus-suscipit-error', 21),
(89, 'quidem omnis', 'eum-et-beatae-cumque-mollitia-ea', 22),
(90, 'minima voluptates non', 'dignissimos-excepturi-provident-magni-ut-esse-quis-alias', 6),
(91, 'sed beatae', 'voluptatem-aliquam-illo-fuga-quia-est-non-itaque', 1),
(92, 'vel explicabo recusandae', 'sunt-sit-itaque-iure-ut-deleniti-eveniet-veritatis-quos', 20),
(95, 'nesciunt', 'consequuntur-nam-placeat-nesciunt-enim', 36),
(97, 'voluptatum molestias', 'et-et-rerum-sunt-est-tempore-ut-exercitationem', 28),
(98, 'eos odio ratione', 'ab-quod-quaerat-voluptates-ratione', 70),
(99, 'commodi cumque', 'reiciendis-odio-nisi-id-consequuntur-architecto-dolores', 90),
(100, 'magnam eius', 'consectetur-repudiandae-ipsum-voluptates-iure', 26),
(101, 'vel', 'sunt-expedita-at-non', 30),
(103, 'molestias', 'ad-porro-quidem-unde-rerum-est-deleniti-quasi', 91),
(107, 'soluta', 'ratione-suscipit-suscipit-mollitia-illum', 100),
(108, 'ut', 'molestiae-commodi-reiciendis-dolores', 21),
(111, 'asperiores', 'ipsam-explicabo-quidem-sit-cum-voluptatem-est', 48),
(114, 'numquam', 'et-quos-quam-molestiae-doloremque-incidunt', 101),
(116, 'voluptate', 'vero-magni-voluptatem-explicabo-perferendis-culpa-tenetur', 75),
(118, 'quisquam minus eius', 'vero-omnis-enim-minima-iste', 98),
(119, 'earum et rem', 'deserunt-necessitatibus-esse-quas-doloribus-corrupti-quia', 13),
(121, 'facere aliquam', 'qui-dolores-vel-nostrum-consectetur-qui-officia', 72),
(122, 'aspernatur quia', 'laudantium-pariatur-et-suscipit', 56),
(123, 'nisi accusantium', 'quasi-rerum-id-nemo-nihil-tempore-quibusdam-illo', 87),
(126, 'error', 'adipisci-doloribus-aut-optio-quo-voluptas-eum-quas', 81),
(127, 'dignissimos qui veritatis', 'sit-rem-non-ipsa-illo', 99),
(132, 'quod', 'aut-corrupti-autem-qui-amet-placeat-deserunt', 18),
(133, 'suscipit maiores natus', 'ad-dolorum-enim-tempore-quia-laudantium-qui', 89),
(134, 'rerum dolores cum', 'dolorem-exercitationem-iste-laboriosam-unde-occaecati-ad-aliquam-ut', 58),
(135, 'iure explicabo harum', 'accusamus-quaerat-fugiat-ut-voluptate-aut', 123),
(137, 'incidunt sed', 'similique-occaecati-quaerat-ratione-architecto-ea-consequuntur', 114),
(140, 'autem officiis', 'sapiente-molestias-nobis-laborum-repellat-iste', 7),
(141, 'quibusdam', 'aspernatur-quia-qui-aliquam-nobis-accusantium', 133),
(143, 'alias', 'tempore-labore-aliquid-quam', 8),
(146, 'aperiam officia', 'et-pariatur-sit-in-tempora-eius', 95),
(149, 'consequatur officia fugiat', 'consequatur-autem-amet-at-quisquam-inventore-quasi-ratione', 31),
(156, 'dolorum possimus', 'velit-repellendus-nihil-consequatur-laborum-ut', 108),
(157, 'occaecati rerum', 'inventore-sed-saepe-vero-ex', 119),
(165, 'ipsam alias', 'natus-error-debitis-eum-ad-est', 92),
(168, 'aut consequuntur dicta', 'in-et-velit-temporibus-voluptatum-dignissimos-doloribus-tenetur', 111),
(169, 'id', 'eos-eos-asperiores-aliquam-dolorum', 40),
(170, 'quia', 'dignissimos-eos-fugiat-consequatur-dolores-et-expedita-illum-atque', 39),
(172, 'sint voluptas', 'laudantium-hic-dignissimos-expedita-molestiae-qui-alias-et-enim', 149),
(174, 'accusamus', 'consequuntur-qui-sed-minima-doloribus', 6),
(178, 'libero incidunt omnis', 'officia-eligendi-qui-aut-ab-id', 83),
(179, 'consequuntur', 'voluptatem-necessitatibus-enim-nobis-ducimus', 107),
(181, 'quia aut quidem', 'qui-reprehenderit-soluta-quis-in-incidunt-necessitatibus-quaerat', 116),
(186, 'quo quia', 'magni-culpa-voluptates-nobis-officiis-est-et-non', 1),
(195, 'nostrum velit rerum', 'pariatur-alias-fugiat-sint-rerum-et-temporibus-non-voluptate', 51),
(200, 'suscipit', 'accusantium-autem-omnis-est-non-minima-omnis', 2),
(201, 'quia rem praesentium', 'voluptas-provident-veritatis-sunt-quia-molestias-id-sit-dolorem', 126),
(202, 'et', 'explicabo-facilis-ut-eum-nostrum-accusantium-aut-minima', 127),
(203, 'voluptatem', 'in-quasi-molestiae-dignissimos-eveniet-voluptate-doloribus-dolorem-eum', 118),
(207, 'omnis iure', 'ducimus-perspiciatis-labore-nam-dolorem-fuga-nostrum-dolor', 27),
(210, 'inventore', 'est-atque-sit-voluptatem-qui', 202),
(218, 'molestiae esse', 'fugit-architecto-iste-voluptatem-eos-non-repellat-voluptate', 9),
(223, 'ad consequatur a', 'qui-cumque-molestias-sed-nulla-est-alias-adipisci', 84),
(225, 'inventore', 'hic-modi-architecto-omnis-consequatur-sequi-voluptas-quia-quo', 41),
(226, 'tenetur cumque', 'dolorem-excepturi-voluptate-sed-animi-labore-ut-rem', 36),
(230, 'aut', 'eos-harum-sed-est-voluptatem', 114),
(231, 'voluptatem hic possimus', 'saepe-autem-expedita-magnam-tempore-aut-consequatur-rerum', 92),
(233, 'aliquid qui', 'rerum-nostrum-eveniet-sint-fugit', 203),
(234, 'itaque aliquid', 'nihil-non-repudiandae-voluptatem-rem-vel-expedita-et', 57),
(239, 'delectus consequuntur unde', 'sequi-eum-dolorem-tenetur-temporibus-labore-eum', 13),
(240, 'ut', 'iste-alias-eos-voluptas-qui-eum-soluta-et', 80),
(251, 'laboriosam sunt delectus', 'sapiente-perferendis-corporis-fugit-omnis-non-officiis-aperiam', 172),
(255, 'necessitatibus quia', 'dolor-totam-ipsum-qui-qui', 146),
(258, 'fugiat ut consectetur', 'nesciunt-quia-tempora-distinctio-atque-officia-voluptatem-illum', 10),
(264, 'possimus', 'fugit-dolores-voluptatem-est-deleniti-dicta-omnis-impedit', 195),
(273, 'voluptates', 'est-sed-tenetur-architecto-architecto', 165),
(283, 'rerum iure minima', 'error-alias-odio-reprehenderit-et-dolor-eum-et', 95),
(285, 'est error laudantium', 'occaecati-qui-dicta-corporis-nostrum', 97),
(289, 'nobis', 'a-deserunt-illo-ea-in-molestias-laboriosam-ut-et', 52),
(290, 'maiores', 'illo-sit-quia-voluptatum-saepe-dolorem-in-est-qui', 50),
(291, 'dolor qui eligendi', 'assumenda-incidunt-consequatur-qui-sit', 289),
(292, 'voluptas molestiae', 'dolore-praesentium-architecto-est-dolor-delectus-velit-minima', 207),
(298, 'molestiae sed cupiditate', 'sapiente-dolorem-necessitatibus-iste-sint-inventore-velit-iusto', 157),
(300, 'nesciunt', 'excepturi-officiis-molestias-consectetur-omnis-recusandae-sequi-molestiae-similique', 168),
(302, 'maiores dolorum', 'amet-reprehenderit-consequuntur-et-sed-est', 223),
(304, 'ipsum porro eaque', 'velit-est-quas-eum-molestiae-vero-voluptate-et', 292),
(305, 'aut iusto excepturi', 'mollitia-quia-molestias-officia-et-nihil-eaque-et', 179),
(310, 'exercitationem', 'sed-aperiam-harum-nesciunt-cum-aliquam-voluptas-iusto', 7),
(315, 'est blanditiis', 'ut-recusandae-eius-sint-sint-quia-voluptatem', 26),
(316, 'et', 'ea-est-qui-et-ipsum-architecto', 181),
(318, 'ratione', 'est-corporis-numquam-debitis-similique', 50),
(325, 'quia', 'et-aut-et-quia-rerum-officiis-in-consequuntur-ipsam', 83),
(326, 'ut', 'incidunt-quas-eum-culpa-ipsam-accusantium', 132),
(329, 'nemo', 'aut-totam-quia-aperiam-excepturi-nisi', 218),
(332, 'molestias in', 'molestiae-harum-et-enim-qui-a', 122),
(335, 'et ut', 'est-amet-non-qui-et-et-quis-earum', 116),
(337, 'vel corporis', 'voluptates-atque-debitis-earum-dolores', 66),
(339, 'est culpa', 'doloribus-quasi-itaque-cupiditate-est-exercitationem', 325),
(343, 'ullam eos iure', 'sint-aliquam-quibusdam-necessitatibus-sint-quo', 169),
(353, 'et', 'sed-nemo-quibusdam-ut-eius-consequatur-enim', 170),
(357, 'magnam', 'sapiente-ut-voluptas-odit-aut', 73),
(364, 'qui saepe', 'molestias-dolorem-occaecati-mollitia-beatae-possimus', 11),
(367, 'id', 'sed-omnis-laudantium-ducimus-eligendi', 51),
(370, 'hic', 'quo-ea-ea-vel', 13),
(378, 'nam a minima', 'et-minima-vero-qui', 143),
(385, 'dolores', 'temporibus-quae-cum-tenetur', 123),
(393, 'et facere', 'ex-et-ut-ipsa-soluta', 46),
(403, 'quaerat', 'aut-saepe-laboriosam-reiciendis-et-optio', 107),
(404, 'molestiae', 'ducimus-dignissimos-accusantium-rerum-rerum-quis-ut', 141),
(405, 'non eos', 'sequi-eaque-aliquid-ullam-iste-inventore-doloribus', 40),
(410, 'aut corrupti', 'est-quae-eaque-laborum-accusamus-ut-quaerat', 174),
(413, 'et', 'cum-quibusdam-et-sit-in-voluptas-quo', 226),
(415, 'ad incidunt', 'tempora-ut-eius-illum-quis', 156),
(428, 'iste', 'et-molestiae-enim-molestias-magni-ea', 37),
(429, 'sit aliquid tempora', 'est-aut-temporibus-quia-similique-beatae-error', 186),
(440, 'incidunt molestiae quidem', 'nostrum-voluptatem-nobis-occaecati-aut-reiciendis-explicabo-aliquid-qui', 258),
(450, 'sunt iusto molestiae', 'possimus-perferendis-delectus-laudantium', 251),
(465, 'deserunt', 'aut-occaecati-dolorem-doloribus-dolorem-quisquam-vel-amet', 233),
(466, 'placeat autem', 'at-et-fuga-aspernatur-aut-inventore-voluptas', 335),
(468, 'incidunt velit et', 'culpa-minus-maxime-quisquam-libero', 169),
(477, 'quia vel', 'et-amet-libero-ipsum-dolorum-voluptates-sequi-commodi', 230),
(490, 'repellat alias', 'soluta-voluptas-commodi-dolorem-accusamus-ut-quo-et', 403),
(492, 'sed illum', 'repellat-labore-corrupti-nulla-molestiae', 468),
(494, 'nesciunt quibusdam cumque', 'aut-nemo-dignissimos-blanditiis-quod-illo-corporis', 137),
(499, 'eos', 'autem-reiciendis-maiores-vel-inventore-eligendi-culpa-commodi', 178),
(501, 'molestiae', 'ut-est-non-possimus-qui-sed-consequuntur', 289),
(502, 'corrupti qui ex', 'ea-voluptatibus-ea-impedit-consequatur', 50),
(503, 'sunt reiciendis quibusdam', 'ipsa-reiciendis-perferendis-quia-eos-eos-facere-voluptas-magnam', 135),
(506, 'perferendis', 'deleniti-aspernatur-et-cupiditate-incidunt-harum-voluptatem', 305),
(508, 'autem', 'ut-deleniti-atque-molestiae-temporibus', 291),
(524, 'dolores consequatur ut', 'dolores-ab-ut-velit-non-qui-inventore-atque', 315),
(532, 'quo aut', 'consequuntur-officia-aut-qui-sequi-excepturi-atque', 440),
(534, 'consequuntur omnis', 'commodi-nam-nihil-atque-facere-omnis', 121),
(551, 'aperiam repellat dolorem', 'accusantium-nemo-qui-quis-illo-quidem-molestiae', 364),
(553, 'quidem', 'optio-in-corrupti-suscipit-velit-nisi-totam', 310),
(559, 'qui dolor est', 'est-ad-qui-quisquam-nihil-ducimus-ea-perspiciatis', 255),
(566, 'laboriosam eum', 'totam-ut-placeat-laboriosam-et-hic-veniam-veniam-tempora', 343),
(567, 'ratione voluptatem', 'unde-officia-voluptates-excepturi-deleniti-dolore', 413),
(571, 'qui fugit nobis', 'ut-ad-laudantium-dolores-reprehenderit-aut-iure-culpa', 499),
(578, 'impedit', 'similique-voluptas-esse-ratione-facilis', 240),
(584, 'expedita dicta', 'at-est-quae-quisquam-possimus-quos', 492),
(604, 'exercitationem quidem et', 'est-quas-et-sunt-et-omnis-repellendus', 15),
(627, 'eum', 'corrupti-nisi-reiciendis-fugiat-repellat-voluptatibus', 357),
(635, 'deserunt', 'placeat-maxime-quasi-laboriosam-nobis', 264),
(638, 'non voluptates similique', 'blanditiis-culpa-consequatur-veniam-qui-soluta-soluta-reiciendis', 532),
(639, 'ipsum dolorem', 'velit-aliquid-aut-qui-beatae-fuga-inventore-nulla', 210),
(644, 'beatae aut', 'omnis-quisquam-exercitationem-distinctio-aut-accusantium-possimus-sint-doloremque', 179),
(653, 'suscipit voluptatem', 'omnis-eum-et-iusto-et', 405),
(658, 'cumque quo assumenda', 'mollitia-fuga-praesentium-consectetur-et-veniam-autem', 234),
(660, 'excepturi voluptatem perferendis', 'culpa-laudantium-voluptatibus-esse-quibusdam-aut-ut', 298),
(664, 'expedita', 'qui-culpa-quo-quis-qui-sed-laboriosam-iste-delectus', 10),
(666, 'quam', 'quos-at-sint-voluptatem-libero', 578),
(674, 'magnam', 'quo-ut-ut-dolore-saepe-rerum-voluptatem-temporibus-quidem', 290),
(685, 'omnis in in', 'debitis-exercitationem-iste-molestiae-ut-autem-est', 566),
(686, 'voluptas soluta sit', 'ea-laborum-quia-saepe-ipsum-vitae-voluptatem', 490),
(693, 'dolorum', 'error-nihil-ut-exercitationem-voluptate-ut-qui-et-est', 178),
(708, 'nihil', 'hic-enim-in-nam', 627),
(722, 'omnis ipsum', 'consequatur-sunt-voluptatem-provident-quisquam-iure-itaque-ipsam-perspiciatis', 8),
(724, 'porro ut nostrum', 'voluptatum-id-eos-in-deleniti-nemo-est', 316),
(725, 'voluptas', 'dicta-aut-consequatur-non-aut-quas', 225),
(733, 'distinctio est', 'sed-natus-dolores-fugiat-doloremque-corporis-qui-qui', 62),
(741, 'distinctio est', 'sed-natus-dolores-fugiat-doloremque', 872),
(755, 'excepturi ut', 'iure-quia-est-a-minus-vitae-reprehenderit', 508),
(761, 'harum', 'quo-non-maiores-facere-accusantium-ut-odit-ipsum', 118),
(763, 'animi ipsam', 'deserunt-quis-in-voluptatum-sed', 724),
(768, 'tempora et', 'omnis-aut-in-deleniti-et-aut', 61),
(786, 'itaque', 'culpa-cumque-et-ullam-ex-quam-fugit-omnis', 5),
(791, 'alias qui ipsam', 'quis-aut-nisi-iusto-voluptas', 132),
(807, 'accusantium voluptatibus', 'dolor-quo-dolorem-odit-fuga', 553),
(827, 'corrupti aut', 'dolore-dolore-assumenda-ea-ipsum-laborum', 231),
(846, 'porro', 'assumenda-maxime-temporibus-praesentium-laudantium-quo-omnis-et-architecto', 450),
(858, 'maxime cupiditate sint', 'recusandae-aliquid-et-impedit-laborum', 316),
(870, 'et', 'hic-aut-consequatur-et-qui-facilis-nihil', 39),
(872, 'iure', 'nihil-laudantium-vel-odit-vel-molestias-velit-tempore', 755),
(879, 'aut repellat', 'maiores-sunt-at-porro-saepe', 524),
(909, 'exercitationem veniam accusantium', 'quas-molestiae-omnis-blanditiis-nihil-quis-in', 370),
(922, 'nostrum vel est', 'aut-numquam-ea-sed-occaecati-eaque', 353),
(949, 'tempore odit', 'possimus-doloribus-similique-ipsam-debitis-est-adipisci-perferendis', 404),
(951, 'delectus at consequatur', 'optio-eum-esse-perspiciatis-dolorem-distinctio-dolor-fugiat', 733),
(953, 'id', 'quia-voluptate-dolor-aliquid', 273),
(967, 'ut non dolor', 'ea-perferendis-repellendus-voluptatibus-repudiandae-quia-harum-tempore-qui', 693),
(976, 'ipsum', 'odit-voluptates-animi-rerum', 494),
(982, 'nulla', 'assumenda-error-facere-voluptate-voluptates-et', 664);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=983;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
