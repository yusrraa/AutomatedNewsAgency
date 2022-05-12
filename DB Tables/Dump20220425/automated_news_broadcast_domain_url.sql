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
-- Table structure for table `domain_url`
--

DROP TABLE IF EXISTS `domain_url`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `domain_url` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category_id` int NOT NULL,
  `url` varchar(600) NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `fk_category_id` (`category_id`),
  CONSTRAINT `fk_category_id` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `domain_url`
--

LOCK TABLES `domain_url` WRITE;
/*!40000 ALTER TABLE `domain_url` DISABLE KEYS */;
INSERT INTO `domain_url` VALUES (1,1,'https://www.dawn.com/sport',1),(2,1,'https://nation.com.pk/sports',1),(3,1,'https://www.thenews.com.pk/latest/category/sports',1),(4,1,'https://sports.ndtv.com/cricket/teams/2116-pakistan-teamprofile/news',0),(5,1,'https://www.geo.tv/category/sports',0),(6,1,'https://tribune.com.pk/sports',0),(7,1,'https://en.dailypakistan.com.pk/sports',0),(8,1,'https://www.newsnow.co.uk/h/Sport',0),(9,1,'https://cricketpakistan.com.pk/en/news',0),(10,1,'https://dunyanews.tv/en/Cricket',0),(11,1,'https://www.bbc.com/sport',0),(12,1,'https://www.pcb.com.pk/news.html',0),(13,1,'https://worldsports.pk/',0),(14,1,'https://timesofindia.indiatimes.com/sports',0),(15,1,'https://arysports.tv/',0),(16,1,'https://www.indiatoday.in/sports',0),(17,1,'https://savedelete.com/category/sports/',0),(18,1,'https://gnnhd.tv/category/sports',0),(19,1,'https://www.republicworld.com/sports-news',0),(20,2,'https://www.dawn.com/tech',1),(21,2,'https://www.thenews.com.pk/latest/category/sci-tech',1),(22,2,'https://www.geo.tv/category/sci-tech',1),(23,2,'https://tribune.com.pk/technology',1);
/*!40000 ALTER TABLE `domain_url` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-25  5:52:06
