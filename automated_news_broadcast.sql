-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 31, 2022 at 02:41 PM
-- Server version: 10.1.39-MariaDB
-- PHP Version: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `automated_news_broadcast`
--

-- --------------------------------------------------------

--
-- Table structure for table `article`
--

CREATE TABLE `article` (
  `id` int(11) NOT NULL,
  `url_id` int(11) NOT NULL,
  `article_url` varchar(767) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `article_img_configuration`
--

CREATE TABLE `article_img_configuration` (
  `id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `tag_name` varchar(20) NOT NULL,
  `scrape_type` varchar(20) NOT NULL,
  `attribute_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `article_publish_date_configuration`
--

CREATE TABLE `article_publish_date_configuration` (
  `id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `tag_name` varchar(20) NOT NULL,
  `scrape_type` varchar(20) NOT NULL,
  `attribute_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `article_text_configuration`
--

CREATE TABLE `article_text_configuration` (
  `id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `tag_name` varchar(20) NOT NULL,
  `scrape_type` varchar(20) NOT NULL,
  `attribute_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `article_topic_headline_configuration`
--

CREATE TABLE `article_topic_headline_configuration` (
  `id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `parent_tag_name` varchar(20) NOT NULL,
  `child_tag_name` varchar(20) NOT NULL,
  `scrape_type` varchar(20) NOT NULL,
  `attribute_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `name` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `name`) VALUES
(1, 'Sports'),
(2, 'Technology'),
(3, 'Entertainment');

-- --------------------------------------------------------

--
-- Table structure for table `domain_url`
--

CREATE TABLE `domain_url` (
  `id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `url` varchar(600) NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `unprocesssed_scrape_data`
--

CREATE TABLE `unprocesssed_scrape_data` (
  `id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `unprocessed_news_topic` longtext NOT NULL,
  `unprocessed_news_description` longtext NOT NULL,
  `publication_date` varchar(767) NOT NULL,
  `image_href` varchar(767) NOT NULL,
  `scrape_time_stamp` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `article`
--
ALTER TABLE `article`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `UNIQUE` (`article_url`),
  ADD KEY `fk_url_id` (`url_id`);

--
-- Indexes for table `article_img_configuration`
--
ALTER TABLE `article_img_configuration`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_article_img_id` (`article_id`);

--
-- Indexes for table `article_publish_date_configuration`
--
ALTER TABLE `article_publish_date_configuration`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_article_publish_id` (`article_id`);

--
-- Indexes for table `article_text_configuration`
--
ALTER TABLE `article_text_configuration`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_article_text_id` (`article_id`);

--
-- Indexes for table `article_topic_headline_configuration`
--
ALTER TABLE `article_topic_headline_configuration`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_topic_headline` (`article_id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `domain_url`
--
ALTER TABLE `domain_url`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_category_id` (`category_id`);

--
-- Indexes for table `unprocesssed_scrape_data`
--
ALTER TABLE `unprocesssed_scrape_data`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `UNIQUE` (`article_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `UNIQUE` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `article`
--
ALTER TABLE `article`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `article_img_configuration`
--
ALTER TABLE `article_img_configuration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `article_publish_date_configuration`
--
ALTER TABLE `article_publish_date_configuration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `article_text_configuration`
--
ALTER TABLE `article_text_configuration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `article_topic_headline_configuration`
--
ALTER TABLE `article_topic_headline_configuration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `domain_url`
--
ALTER TABLE `domain_url`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `unprocesssed_scrape_data`
--
ALTER TABLE `unprocesssed_scrape_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `article`
--
ALTER TABLE `article`
  ADD CONSTRAINT `fk_url_id` FOREIGN KEY (`url_id`) REFERENCES `domain_url` (`id`);

--
-- Constraints for table `article_img_configuration`
--
ALTER TABLE `article_img_configuration`
  ADD CONSTRAINT `fk_article_img_id` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`);

--
-- Constraints for table `article_publish_date_configuration`
--
ALTER TABLE `article_publish_date_configuration`
  ADD CONSTRAINT `fk_article_publish_id` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`);

--
-- Constraints for table `article_text_configuration`
--
ALTER TABLE `article_text_configuration`
  ADD CONSTRAINT `fk_article_id` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`),
  ADD CONSTRAINT `fk_article_pub_id` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`),
  ADD CONSTRAINT `fk_article_text_id` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`);

--
-- Constraints for table `article_topic_headline_configuration`
--
ALTER TABLE `article_topic_headline_configuration`
  ADD CONSTRAINT `fk_topic_headline` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`);

--
-- Constraints for table `domain_url`
--
ALTER TABLE `domain_url`
  ADD CONSTRAINT `fk_category_id` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`);

--
-- Constraints for table `unprocesssed_scrape_data`
--
ALTER TABLE `unprocesssed_scrape_data`
  ADD CONSTRAINT `fk_article_unprocessed_id` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
