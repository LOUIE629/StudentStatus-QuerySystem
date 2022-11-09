-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: student
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Temporary view structure for view `01shujuku`
--

DROP TABLE IF EXISTS `01shujuku`;
/*!50001 DROP VIEW IF EXISTS `01shujuku`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `01shujuku` AS SELECT 
 1 AS `SNO`,
 1 AS `SNAME`,
 1 AS `SSEX`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `c`
--

DROP TABLE IF EXISTS `c`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `c` (
  `CNO` char(10) NOT NULL,
  `CNAME` varchar(45) NOT NULL,
  `CREDIT` varchar(45) NOT NULL,
  PRIMARY KEY (`CNO`),
  KEY `IX_CName` (`CNAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `c`
--

LOCK TABLES `c` WRITE;
/*!40000 ALTER TABLE `c` DISABLE KEYS */;
INSERT INTO `c` VALUES ('1','数据库','3'),('2','高等数学','5'),('3','信息系统','2'),('4','操作系统','3'),('5','数据系统','3'),('6','C语言','2');
/*!40000 ALTER TABLE `c` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `s`
--

DROP TABLE IF EXISTS `s`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `s` (
  `SNO` char(10) NOT NULL,
  `SNAME` char(20) NOT NULL,
  `SSEX` char(2) NOT NULL DEFAULT '男',
  `SBIRTH` varchar(10) NOT NULL,
  `SDEPT` char(20) NOT NULL,
  PRIMARY KEY (`SNO`),
  UNIQUE KEY `SNO_UNIQUE` (`SNO`),
  UNIQUE KEY `SNAME_UNIQUE` (`SNAME`),
  KEY `IX_ngd` (`SNAME`,`SSEX`,`SDEPT`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `s`
--

LOCK TABLES `s` WRITE;
/*!40000 ALTER TABLE `s` DISABLE KEYS */;
INSERT INTO `s` VALUES ('2018300356','小辰','男','2000/06/29','10'),('2018300357','阿康','男','2001/06/01','1'),('2018300358','冰冰','女','1999/10/01','1'),('2018300359','豪昊','男','1997/05/21','3'),('2018300360','啦啦啦','男','2000/6/6','2');
/*!40000 ALTER TABLE `s` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sc`
--

DROP TABLE IF EXISTS `sc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sc` (
  `sno` char(10) NOT NULL,
  `cno` char(10) NOT NULL,
  `grade` varchar(45) NOT NULL,
  KEY `sc_cno_idx` (`cno`),
  KEY `sc_sno_idx` (`sno`),
  CONSTRAINT `sc_cno` FOREIGN KEY (`cno`) REFERENCES `c` (`CNO`),
  CONSTRAINT `sc_sno` FOREIGN KEY (`sno`) REFERENCES `s` (`SNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sc`
--

LOCK TABLES `sc` WRITE;
/*!40000 ALTER TABLE `sc` DISABLE KEYS */;
INSERT INTO `sc` VALUES ('2018300356','3','90'),('2018300357','1','70'),('2018300357','2','100'),('2018300358','1','100'),('2018300358','2','90'),('2018300358','2','90'),('2018300356','1','70');
/*!40000 ALTER TABLE `sc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'student'
--

--
-- Dumping routines for database 'student'
--

--
-- Final view structure for view `01shujuku`
--

/*!50001 DROP VIEW IF EXISTS `01shujuku`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = gbk */;
/*!50001 SET character_set_results     = gbk */;
/*!50001 SET collation_connection      = gbk_chinese_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `01shujuku` AS select `s`.`SNO` AS `SNO`,`s`.`SNAME` AS `SNAME`,`s`.`SSEX` AS `SSEX` from `s` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-20 21:41:40
