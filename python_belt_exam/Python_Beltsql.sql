-- MySQL dump 10.13  Distrib 8.0.29, for macos12 (x86_64)
--
-- Host: localhost    Database: python_belt
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `shows`
--

DROP TABLE IF EXISTS `shows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shows` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `network` varchar(255) DEFAULT NULL,
  `release_date` varchar(255) DEFAULT NULL,
  `description` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_shows_users_idx` (`user_id`),
  CONSTRAINT `fk_shows_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shows`
--

LOCK TABLES `shows` WRITE;
/*!40000 ALTER TABLE `shows` DISABLE KEYS */;
INSERT INTO `shows` VALUES (1,'The Office','NBC','2005-03-04','A mockumantry about ordinary company\r\nThis part is updated','2022-09-15 13:45:25','2022-09-15 13:45:25',4),(2,'Strange Things','Netflix','2016-07-15','This show have no description. But can be updated anytime','2022-09-15 13:57:54','2022-09-15 13:57:54',4),(3,'Saturday Night Live','NBC','1975-10-11','Saturday Night live is aired from NY every saturday...I gues','2022-09-15 14:01:48','2022-09-15 14:01:48',1),(4,'Silicon Valley','HBO','2014-04-06','Silicon Valley Based....TV show','2022-09-15 14:03:58','2022-09-15 14:03:58',1),(6,'Avatar the last Air Bender','Nickeloden','2005-02-21','The Avatar the Last air is the show based in NY...','2022-09-15 14:34:40','2022-09-15 14:34:40',2);
/*!40000 ALTER TABLE `shows` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` varchar(45) DEFAULT 'NOW()',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Gosa','Dadi','gosadadi@gmail.com','$2b$12$3Gd8BTgCHMM/CqiM2rSpLu6vHjMf87hHu6cENPU1fBkkovHddExaq','2022-09-15 09:55:12','2022-09-15 09:55:12'),(2,'Howdy ','Jenna','howdyjenna@gmail.com','$2b$12$3g5SpeC1iDrWtMVCE4U5rusVIjlRWyDp2xdcquIX./dGkogtzN4d2','2022-09-15 10:39:20','2022-09-15 10:39:20'),(3,'Anne','Davies','annadavies@gmail.com','$2b$12$ggPHXEi2s8jpFMReJfe0yu0NSFbwozeZv9UnDA1Y6gHwRT39NDp.m','2022-09-15 10:41:36','2022-09-15 10:41:36'),(4,'Anne','Davies','AnneDavies@gmail.com','$2b$12$y3HxDumm2QsU/T48jGcfPeC1IDJ6RdOudrpy1TSnn2D/DPu5wJeyq','2022-09-15 11:59:33','2022-09-15 11:59:33'),(5,'mike','mazur','mike@mail.com','$2b$12$VcXxbSv9BbiZKMGPlmWvZu3Kt8Rt8Ap9J2sdF6bGKhDEpjEV3OSeW','2022-09-15 12:44:36','2022-09-15 12:44:36');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-15 15:23:41
