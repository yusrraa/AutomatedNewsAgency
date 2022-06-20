-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: automated_news_broadcast
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `article_topic_headline_configuration`
--

DROP TABLE IF EXISTS `article_topic_headline_configuration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `article_topic_headline_configuration` (
  `id` int NOT NULL AUTO_INCREMENT,
  `domain_url_id` int NOT NULL,
  `parent_tag_name` varchar(20) NOT NULL,
  `child_tag_name` varchar(20) NOT NULL,
  `scrape_type` varchar(20) NOT NULL,
  `attribute_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_topic_head_config` (`domain_url_id`),
  CONSTRAINT `fk_topic_head_config` FOREIGN KEY (`domain_url_id`) REFERENCES `domain_url` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article_topic_headline_configuration`
--

LOCK TABLES `article_topic_headline_configuration` WRITE;
/*!40000 ALTER TABLE `article_topic_headline_configuration` DISABLE KEYS */;
INSERT INTO `article_topic_headline_configuration` VALUES (1,1,'h2','a','class','story__title'),(2,2,'section','h1','class','singlepost'),(3,3,'div','h1','class','detail-heading'),(4,6,'div','h1','class','story-box-section'),(5,20,'h2','a','class','story__title'),(6,21,'div','h1','class','detail-heading'),(7,22,'div','h1','class','story-area'),(8,23,'div','h1','class','story-box-section');
/*!40000 ALTER TABLE `article_topic_headline_configuration` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-25  5:52:07
