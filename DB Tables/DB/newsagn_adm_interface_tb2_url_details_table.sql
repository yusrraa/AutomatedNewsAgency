-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: newsagn
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `adm_interface_tb2_url_details_table`
--

DROP TABLE IF EXISTS `adm_interface_tb2_url_details_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adm_interface_tb2_url_details_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `article_url` varchar(100) NOT NULL,
  `url_string` varchar(200) NOT NULL,
  `domain_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `adm_interface_tb2_ur_domain_id_290a43ef_fk_adm_inter` (`domain_id`),
  CONSTRAINT `adm_interface_tb2_ur_domain_id_290a43ef_fk_adm_inter` FOREIGN KEY (`domain_id`) REFERENCES `adm_interface_tb1_master_domain` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adm_interface_tb2_url_details_table`
--

LOCK TABLES `adm_interface_tb2_url_details_table` WRITE;
/*!40000 ALTER TABLE `adm_interface_tb2_url_details_table` DISABLE KEYS */;
INSERT INTO `adm_interface_tb2_url_details_table` VALUES (11,'','www.dawn.com/sports',72),(12,'','www.dawn.com/sports',72);
/*!40000 ALTER TABLE `adm_interface_tb2_url_details_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-18 16:58:03
