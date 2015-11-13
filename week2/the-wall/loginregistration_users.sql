-- MySQL dump 10.13  Distrib 5.6.24, for osx10.8 (x86_64)
--
-- Host: 127.0.0.1    Database: loginregistration
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `idusers` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`idusers`),
  UNIQUE KEY `idusers_UNIQUE` (`idusers`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'d','l','test@gmail.com','$2b$12$slfN0LYcEQFhlnGdVOCJfOCosWsBLr/r41OLxt\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 13:28:22','2015-11-12 13:28:22'),(3,'Danielle','Leong','d@gmail.com','$2b$12$vtLsOU1C2I6XCx1.jpKA/u06vmhncSkUUY6qBn\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 13:38:47','2015-11-12 13:38:47'),(4,'Test three','last name','test@t.com','$2b$12$XMCiEVEQ6XrQxeofY/rJpOJSOfJl6m.Or/G1Z.\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 15:33:24','2015-11-12 15:33:24'),(5,'Danielle','Leong','d@test.com','$2b$12$aQaur2elQmJACiZMRbbhruas7z6f2zSjdHVQKb\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 15:34:32','2015-11-12 15:34:32'),(6,'Danielle test','test','test@test.com','$2b$12$KqJGi7N0cjxwvlLLf.sB2uCfCDL10pTgugoGem\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 16:17:05','2015-11-12 16:17:05'),(7,'DanielleL','L','test@d.com','$2b$12$s7tbTeTjVEgh/tK6YeQp9.8EwbBFf0szUGhGnx\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 16:22:32','2015-11-12 16:22:32'),(9,'Test','Test','test3@gmail.com','$2b$12$DkVi7Iq19dPVsdrR/4ombuQKjBmjvaE8qR4MEF\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 16:43:32','2015-11-12 16:43:32'),(10,'Danielle','Leong','d@d.com','$2b$12$DQV3yNzfVqkhb7RYjNoiNOxrbc667ZXuUEE.Ky\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 17:13:29','2015-11-12 17:13:29'),(11,'Test four','test','t@test.com','$2b$12$ksWQcV7hWQgvjZ.dKIPZceb/ic5V5UljcTKyTH\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 17:54:03','2015-11-12 17:54:03'),(12,'Danielle','Leong','t@t.com','$2b$12$AlLpraVMfiMhIbnc1qypU.22GXuXBBcBIErZpa\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 18:30:54','2015-11-12 18:30:54'),(13,'User','Name','user@test.com','$2b$12$w5C61XP56bdtYp1eysYcIO7rYdwt9RM2f6PtUh\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 18:38:10','2015-11-12 18:38:10'),(14,'D','Leong','u@test.com','$2b$12$bd1jrBZiF1FLlC530xx09.YUq4.cCD794aiUa/\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 18:42:30','2015-11-12 18:42:30'),(15,'DL','LL','a@test.com','$2b$12$04BKDAIPHC03EqR/hJYKaezzRxpLSoOgANO/af\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 18:44:12','2015-11-12 18:44:12'),(16,'Userr','Test','b@test.com','$2b$12$6I.FrOA9L8imqAfR20996Ou1cLDS.gHUCDCjk5\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 18:45:55','2015-11-12 18:45:55'),(17,'New','User','c@test.com','$2b$12$EGxPwEnQ9R6JFe1iul1ElevDebmoLcuvixQs.O\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 18:51:04','2015-11-12 18:51:04'),(18,'New','User','e@test.com','$2b$12$TNTWkEkUfUVAsxyTrg1KcO8LGCAhdbNtNzFHrk\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 18:58:48','2015-11-12 18:58:48'),(19,'F','User','f@test.com','$2b$12$UL6Dd2MWEnftWQrplUSCKetlngsZGHSBC2nhTp\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','2015-11-12 18:59:45','2015-11-12 18:59:45'),(20,'G','User','g@test.com','$2b$12$Z0TNcXshA8S1TmmDqGj/7eB2JfWuymaUbBJSsMpF8FNDV2XwkJdF6','2015-11-12 19:03:22','2015-11-12 19:03:22'),(21,'H','User','h@test.com','$2b$12$sI7EQuFrDr6Znp1howleHeW9/6p8Ov0PCEcceBND4CigEFne6/r/i','2015-11-12 19:13:37','2015-11-12 19:13:37'),(22,'Danielle','Leong','i@test.com','$2b$12$/ZqJCx3kcIACyU2gdZOBO.8Zwy4OX5/3Iqrc9.0D5PLlOoh5OmJKS','2015-11-13 11:40:53','2015-11-13 11:40:53');
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

-- Dump completed on 2015-11-13 11:52:41
