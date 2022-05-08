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
-- Table structure for table `article_img_configuration`
--

DROP TABLE IF EXISTS `article_img_configuration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `article_img_configuration` (
  `id` int NOT NULL AUTO_INCREMENT,
  `domain_url_id` int NOT NULL,
  `tag_name` varchar(20) NOT NULL,
  `scrape_type` varchar(20) NOT NULL,
  `attribute_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_img_config` (`domain_url_id`),
  CONSTRAINT `fk_img_config` FOREIGN KEY (`domain_url_id`) REFERENCES `domain_url` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article_img_configuration`
--

LOCK TABLES `article_img_configuration` WRITE;
/*!40000 ALTER TABLE `article_img_configuration` DISABLE KEYS */;
INSERT INTO `article_img_configuration` VALUES (1,1,'div','class','media__item'),(2,2,'div','class','imgpost'),(3,3,'div','class','medium-insert-images'),(4,6,'div','class','amp-top-main-img'),(5,20,'div','class','media__item'),(6,21,'div','class','medium-insert-images'),(7,22,'div','class','medium-insert-images'),(8,23,'div','class','amp-top-main-img');
/*!40000 ALTER TABLE `article_img_configuration` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-25  5:52:04
