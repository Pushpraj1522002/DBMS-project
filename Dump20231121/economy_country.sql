-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: economy
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `country` (
  `Country_Id` varchar(10) NOT NULL,
  `Country_Name` varchar(50) NOT NULL,
  `Status` int NOT NULL,
  `Continent_Id` varchar(10) NOT NULL,
  PRIMARY KEY (`Country_Id`),
  KEY `country_ibfk_1` (`Continent_Id`),
  CONSTRAINT `country_ibfk_1` FOREIGN KEY (`Continent_Id`) REFERENCES `continent` (`Continent_Id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
INSERT INTO `country` VALUES ('AR','ARGENTINA',0,'LAC'),('AT','AUSTR',0,'AT'),('BD','Bangladesh',0,'AS'),('BG','BULGARIA',0,'EU'),('BR','BRAZIL',0,'LAC'),('BS','THE BAHAMAS',0,'LAC'),('BT','BHUTAN',0,'AS'),('BY','BELARUS',0,'EU'),('CD','D.R.CONGO',0,'AF'),('CL','CHILE',1,'LAC'),('CN','CHINA',1,'AS'),('CO','COLOMBIA',0,'LAC'),('CR','COAST RICA',1,'LAC'),('GH','GHANA',0,'AF'),('HU','HUNGARY',1,'EU'),('ID','INDONESIA',0,'AS'),('IN','INDIA',0,'AS'),('KE','KENYA',0,'AF'),('LK','SRILANKA',0,'AS'),('LR','LIBERIA',0,'AF'),('MD','MOLDOVA',0,'EU'),('MG','MADAGASCAR',0,'AF'),('MU','MAURITIUS',1,'AF'),('MX','MEXICO',0,'LAC'),('MY','MALAYSIA',0,'AS'),('NA','Namibia',0,'AF'),('NG','NIGERIA',0,'AF'),('NP','NEPAL',0,'AS'),('PE','PERU',0,'LAC'),('PL','POLAND',1,'EU'),('PY','PARAGUAY',0,'LAC'),('RO','ROMANIA',0,'EU'),('RS','SERBIA',0,'EU'),('SV','EL SALVADOR',0,'LAC'),('TH','THAILAND',0,'AS'),('TY','TURKEY',0,'EU'),('UA','UKRAINE',0,'EU'),('VN','VIETNAM',0,'AS'),('XK','KOSOVO',0,'EU'),('ZM','ZAMBIA',0,'AF'),('ZW','ZIMBABWE',0,'AF');
/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-21 15:13:27
