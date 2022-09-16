-- MySQL dump 10.13  Distrib 8.0.29, for macos12 (x86_64)
--
-- Host: localhost    Database: user_recipe
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
-- Table structure for table `recipes`
--

DROP TABLE IF EXISTS `recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` text,
  `instructions` text,
  `under_thirty` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_recipes_users_idx` (`user_id`),
  CONSTRAINT `fk_recipes_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
INSERT INTO `recipes` VALUES (3,2,'Garlic ','A side dish that goes well with most postos','Mix together fresh chopped garlic and butter. Slice French roll length-wise. Spread butter and garlic on bread halves.\r\n                            ','yes','2022-09-12 00:00:00','2022-09-15 09:36:03'),(4,2,'Spam Musubi','A delicious Hawaiian favorite','Cook the rice. Pan fry several slices of spam. When rice and spam are done, distribute a row of rice a half_inch from the the fridge of the sushi paper. Layer spam on the top. Roll, and enjoy','yes','2022-07-05 00:00:00','2022-09-14 19:37:20'),(5,3,'CheeseCake','Delicious cheesecake','No need to prepare. just eat','no','2022-01-04 00:00:00','2022-09-14 21:24:47');
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
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
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Abebe','Balcha','Balcha2022@gmail.com','$2b$12$YArQ7v.KeUE0IHm34LBIH.sBsEZ1G.lezeEuC1clmRs.ptLP7cP/.','2022-09-12 17:19:09','2022-09-12 17:19:09'),(2,'Alana','Joe','alanajoe@gmail.com','$2b$12$9AYkF/Zv97dcoBRGXNZZKu3NpY8s9f6Q0pstROKziT7O/Y97qNVhq','2022-09-12 18:58:35','2022-09-12 18:58:35'),(3,'Kai','Gudata','KaiGudata@gmail.com','$2b$12$Y11wFdLqC1OXYlpcqG/dLuoiJpajgF/n2DGwPH7.JvaH99iiEBmYW','2022-09-12 19:01:14','2022-09-12 19:01:14'),(4,'Rajan','Raaji','RajanRaaji@gmail.com','$2b$12$vPtxCK//JFbuBf8buRSIsub74KhhSiWfEwD.5FQgycQ87stTwdUW6','2022-09-12 19:02:46','2022-09-12 19:02:46'),(5,'Gosa','Dadi','gosadadi@gmail.com','$2b$12$eeVWIbEk.SBR9fF0vwPoV.s4dJUmE9ErBL3nb0DomepDDCUq5E0Ou','2022-09-14 19:41:27','2022-09-14 19:41:27');
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

-- Dump completed on 2022-09-15  9:45:24
