-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 01, 2022 at 12:19 PM
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
  `domain_url_id` int(11) NOT NULL,
  `tag_name` varchar(20) NOT NULL,
  `scrape_type` varchar(20) NOT NULL,
  `attribute_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `article_img_configuration`
--

INSERT INTO `article_img_configuration` (`id`, `domain_url_id`, `tag_name`, `scrape_type`, `attribute_name`) VALUES
(1, 1, 'div', 'class', 'media__item'),
(2, 2, 'div', 'class', 'imgpost'),
(3, 3, 'div', 'class', 'medium-insert-images'),
(4, 6, 'div', 'class', 'amp-top-main-img'),
(5, 20, 'div', 'class', 'media__item'),
(6, 21, 'div', 'class', 'medium-insert-images'),
(7, 22, 'div', 'class', 'medium-insert-images'),
(8, 23, 'div', 'class', 'amp-top-main-img');


-- --------------------------------------------------------

--
-- Table structure for table `article_publish_date_configuration`
--

CREATE TABLE `article_publish_date_configuration` (
  `id` int(11) NOT NULL,
  `domain_url_id` int(11) NOT NULL,
  `tag_name` varchar(20) NOT NULL,
  `scrape_type` varchar(20) NOT NULL,
  `attribute_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `article_publish_date_configuration`
--

INSERT INTO `article_publish_date_configuration` (`id`, `domain_url_id`, `tag_name`, `scrape_type`, `attribute_name`) VALUES
(1, 1, 'span', 'class', 'story__time'),
(2, 2, 'p', 'class', 'meta-date'),
(3, 3, 'div', 'class', 'category-date'),
(4, 6, 'div', 'class', 'left-authorbox'),
(5, 20, 'span', 'class', 'story__time'),
(6, 21, 'div', 'class', 'category-date'),
(7, 22, 'p', 'class', 'post-date-time'),
(8, 23, 'div', 'class', 'left-authorbox');

-- --------------------------------------------------------

--
-- Table structure for table `article_text_configuration`
--

CREATE TABLE `article_text_configuration` (
  `id` int(11) NOT NULL,
  `domain_url_id` int(11) NOT NULL,
  `tag_name` varchar(20) NOT NULL,
  `scrape_type` varchar(20) NOT NULL,
  `attribute_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `article_text_configuration`
--

INSERT INTO `article_text_configuration` (`id`, `domain_url_id`, `tag_name`, `scrape_type`, `attribute_name`) VALUES
(1, 1, 'div', 'class', 'story__content'),
(2, 2, 'div', 'class', 'post-content'),
(3, 3, 'div', 'class', 'story-detail'),
(4, 6, 'div', 'class', 'story-text'),
(5, 20, 'div', 'class', 'story__content'),
(6, 21, 'div', 'class', 'story-detail'),
(7, 22, 'div', 'class', 'content-area'),
(8, 23, 'div', 'class', 'story-text');

-- --------------------------------------------------------

--
-- Table structure for table `article_topic_headline_configuration`
--

CREATE TABLE `article_topic_headline_configuration` (
  `id` int(11) NOT NULL,
  `domain_url_id` int(11) NOT NULL,
  `parent_tag_name` varchar(20) NOT NULL,
  `child_tag_name` varchar(20) NOT NULL,
  `scrape_type` varchar(20) NOT NULL,
  `attribute_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `article_topic_headline_configuration`
--

INSERT INTO `article_topic_headline_configuration` (`id`, `domain_url_id`, `parent_tag_name`, `child_tag_name`, `scrape_type`, `attribute_name`) VALUES
(1, 1, 'h2', 'a', 'class', 'story__title'),
(2, 2, 'section', 'h1', 'class', 'singlepost'),
(3, 3, 'div', 'h1', 'class', 'detail-heading'),
(4, 6, 'div', 'h1', 'class', 'story-box-section'),
(5, 20, 'h2', 'a', 'class', 'story__title'),
(6, 21, 'div', 'h1', 'class', 'detail-heading'),
(7, 22, 'div', 'h1', 'class', 'story-area'),
(8, 23, 'div', 'h1', 'class', 'story-box-section');

-- --------------------------------------------------------

--
-- Table structure for table `article_url_configuration`
--

CREATE TABLE `article_url_configuration` (
  `id` int(11) NOT NULL,
  `domain_url_id` int(11) NOT NULL,
  `tag_name` varchar(20) NOT NULL,
  `scrape_type` varchar(20) NOT NULL,
  `attribute_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `article_url_configuration`
--

INSERT INTO `article_url_configuration` (`id`, `domain_url_id`, `tag_name`, `scrape_type`, `attribute_name`) VALUES
(1, 1, 'div', 'class', 'w-full'),
(2, 2, 'div', 'class', 'blogtwo'),
(3, 3, 'div', 'class', 'detail-center'),
(4, 6, 'div', 'class', 'container'),
(5, 20, 'div', 'class', 'w-full'),
(6, 21, 'div', 'class', 'most-popular'),
(7, 22, 'div', 'class', 'latest-content'),
(8, 23, 'div', 'class', 'container');

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

--
-- Dumping data for table `domain_url`
--

INSERT INTO `domain_url` (`id`, `category_id`, `url`, `is_active`) VALUES
(1, 1, 'https://www.dawn.com/sport', 1),
(2, 1, 'https://nation.com.pk/sports', 1),
(3, 1, 'https://www.thenews.com.pk/latest/category/sports', 1),
(4, 1, 'https://sports.ndtv.com/cricket/teams/2116-pakistan-teamprofile/news', 0),
(5, 1, 'https://www.geo.tv/category/sports', 0),
(6, 1, 'https://tribune.com.pk/sports', 0),
(7, 1, 'https://en.dailypakistan.com.pk/sports', 0),
(8, 1, 'https://www.newsnow.co.uk/h/Sport', 0),
(9, 1, 'https://cricketpakistan.com.pk/en/news', 0),
(10, 1, 'https://dunyanews.tv/en/Cricket', 0),
(11, 1, 'https://www.bbc.com/sport', 0),
(12, 1, 'https://www.pcb.com.pk/news.html', 0),
(13, 1, 'https://worldsports.pk/', 0),
(14, 1, 'https://timesofindia.indiatimes.com/sports', 0),
(15, 1, 'https://arysports.tv/', 0),
(16, 1, 'https://www.indiatoday.in/sports', 0),
(17, 1, 'https://savedelete.com/category/sports/', 0),
(18, 1, 'https://gnnhd.tv/category/sports', 0),
(19, 1, 'https://www.republicworld.com/sports-news', 0),
(20, 2, 'https://www.dawn.com/tech', 1),
(21, 2, 'https://www.thenews.com.pk/latest/category/sci-tech', 1),
(22, 2, 'https://www.geo.tv/category/sci-tech', 1),
(23, 2, 'https://tribune.com.pk/technology', 1);

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
  `scrape_date_stamp` Varchar(20) NOT NULL,
  `scrape_time_stamp` Varchar(20) NOT NULL
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
  ADD KEY `fk_img_config` (`domain_url_id`);

--
-- Indexes for table `article_publish_date_configuration`
--
ALTER TABLE `article_publish_date_configuration`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_pub_date_config` (`domain_url_id`);

--
-- Indexes for table `article_text_configuration`
--
ALTER TABLE `article_text_configuration`
  ADD PRIMARY KEY (`id`),
  ADD KEY `domain_url_id` (`domain_url_id`);

--
-- Indexes for table `article_topic_headline_configuration`
--
ALTER TABLE `article_topic_headline_configuration`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_topic_head_config` (`domain_url_id`);

--
-- Indexes for table `article_url_configuration`
--
ALTER TABLE `article_url_configuration`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_url_config` (`domain_url_id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `article_publish_date_configuration`
--
ALTER TABLE `article_publish_date_configuration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `article_text_configuration`
--
ALTER TABLE `article_text_configuration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `article_topic_headline_configuration`
--
ALTER TABLE `article_topic_headline_configuration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `article_url_configuration`
--
ALTER TABLE `article_url_configuration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `domain_url`
--
ALTER TABLE `domain_url`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

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
  ADD CONSTRAINT `fk_img_config` FOREIGN KEY (`domain_url_id`) REFERENCES `domain_url` (`id`);

--
-- Constraints for table `article_publish_date_configuration`
--
ALTER TABLE `article_publish_date_configuration`
  ADD CONSTRAINT `fk_pub_date_config` FOREIGN KEY (`domain_url_id`) REFERENCES `domain_url` (`id`);

--
-- Constraints for table `article_text_configuration`
--
ALTER TABLE `article_text_configuration`
  ADD CONSTRAINT `fk_txt_config` FOREIGN KEY (`domain_url_id`) REFERENCES `domain_url` (`id`);

--
-- Constraints for table `article_topic_headline_configuration`
--
ALTER TABLE `article_topic_headline_configuration`
  ADD CONSTRAINT `fk_topic_head_config` FOREIGN KEY (`domain_url_id`) REFERENCES `domain_url` (`id`);

--
-- Constraints for table `article_url_configuration`
--
ALTER TABLE `article_url_configuration`
  ADD CONSTRAINT `fk_url_config` FOREIGN KEY (`domain_url_id`) REFERENCES `domain_url` (`id`);

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