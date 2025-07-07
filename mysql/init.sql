-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: db_biblioteca_v1
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `autores`
--

DROP TABLE IF EXISTS `autores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `autores` (
  `autor_id` int(11) NOT NULL AUTO_INCREMENT,
  `autor_nom` varchar(250) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `usuario_creacion_id` int(11) DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  `usuario_actualizacion_id` int(11) DEFAULT NULL,
  `estado_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`autor_id`),
  KEY `fk_autores_creacion` (`usuario_creacion_id`),
  KEY `fk_autores_actualizacion` (`usuario_actualizacion_id`),
  KEY `estado_id` (`estado_id`),
  CONSTRAINT `autores_ibfk_1` FOREIGN KEY (`estado_id`) REFERENCES `estado` (`estado_id`),
  CONSTRAINT `fk_autores_actualizacion` FOREIGN KEY (`usuario_actualizacion_id`) REFERENCES `usuarios` (`usuario_id`),
  CONSTRAINT `fk_autores_creacion` FOREIGN KEY (`usuario_creacion_id`) REFERENCES `usuarios` (`usuario_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autores`
--

LOCK TABLES `autores` WRITE;
/*!40000 ALTER TABLE `autores` DISABLE KEYS */;
INSERT INTO `autores` VALUES (1,'Gabriel García Márquez','2025-05-14 00:33:27',1,'2025-06-24 20:26:34',1,1),(2,'Isabel Allende','2025-05-14 00:33:27',1,'2025-06-24 22:19:12',1,1),(3,'Mario Vargas Llosa','2025-05-14 00:33:27',1,'2025-06-27 22:31:06',1,2),(4,'Julio Cortázar','2025-05-14 00:33:27',1,'2025-05-14 00:33:27',1,1),(5,'Laura Esquivel','2025-05-14 00:33:27',1,'2025-05-14 00:33:27',1,1),(6,'Jorge Luis Borges','2025-05-14 00:33:27',1,'2025-05-14 00:33:27',1,1),(7,'Carlos Fuentes','2025-05-14 00:33:27',1,'2025-05-14 00:33:27',1,1),(8,'Pablo Neruda','2025-05-14 00:33:27',1,'2025-05-14 00:33:27',1,1),(9,'Rosa Montero','2025-05-14 00:33:27',1,'2025-05-14 00:33:27',1,1),(10,'kentaro miura','2025-05-14 00:33:27',1,'2025-06-24 20:23:53',1,1),(11,'Gabriel García Márquez','2025-06-09 17:39:49',1,NULL,NULL,1),(12,'akira toriyama','2025-06-09 19:46:14',1,NULL,NULL,1),(13,'kentaro miura','2025-06-09 19:53:53',1,NULL,NULL,1),(14,'Miyazaki','2025-06-09 23:09:22',1,NULL,NULL,1),(15,'Minato Namikaze','2025-06-09 23:13:46',1,NULL,NULL,1),(16,'kentaro miura','2025-06-19 14:21:45',1,'2025-06-27 17:38:30',1,2),(17,'kentaro miura','2025-06-24 20:20:21',1,NULL,NULL,1),(18,'kentaro miura','2025-06-24 20:23:29',1,'2025-06-27 17:38:25',1,2),(19,'akira yamaoka','2025-06-24 23:08:12',1,'2025-06-29 13:34:14',1,2);
/*!40000 ALTER TABLE `autores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorias` (
  `categoria_id` int(11) NOT NULL AUTO_INCREMENT,
  `categoria_nom` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`categoria_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (1,'Ficción'),(2,'No Ficción'),(3,'Ciencia'),(4,'Tecnología'),(5,'Historia'),(6,'Biografía'),(7,'Fantasía'),(8,'Romance'),(9,'Arte'),(10,'Educación');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editoriales`
--

DROP TABLE IF EXISTS `editoriales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `editoriales` (
  `editorial_id` int(11) NOT NULL AUTO_INCREMENT,
  `editorial_nom` varchar(250) DEFAULT NULL,
  `estado_id` int(11) DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  `usuario_actualizacion_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`editorial_id`),
  KEY `estado_id` (`estado_id`),
  KEY `usuario_actualizacion_id` (`usuario_actualizacion_id`),
  CONSTRAINT `editoriales_ibfk_1` FOREIGN KEY (`estado_id`) REFERENCES `estado` (`estado_id`),
  CONSTRAINT `editoriales_ibfk_2` FOREIGN KEY (`usuario_actualizacion_id`) REFERENCES `usuarios` (`usuario_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editoriales`
--

LOCK TABLES `editoriales` WRITE;
/*!40000 ALTER TABLE `editoriales` DISABLE KEYS */;
INSERT INTO `editoriales` VALUES (1,'Penguin Random House 2',1,NULL,NULL),(2,'HarperCollins',1,NULL,NULL),(3,'Grupo Planeta',2,NULL,NULL),(4,'Santillana',1,NULL,NULL),(5,'McGraw-Hill',1,NULL,NULL),(6,'Editorial Norma',1,NULL,NULL),(7,'Ediciones SM',1,NULL,NULL),(8,'Anagrama',1,NULL,NULL),(9,'Alfaguara',1,NULL,NULL),(10,'Siglo XXI Editores',1,NULL,NULL),(11,'planetita',1,NULL,NULL),(12,'saiyan house',2,'2025-06-29 13:39:44',1);
/*!40000 ALTER TABLE `editoriales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado`
--

DROP TABLE IF EXISTS `estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado` (
  `estado_id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`estado_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado`
--

LOCK TABLES `estado` WRITE;
/*!40000 ALTER TABLE `estado` DISABLE KEYS */;
INSERT INTO `estado` VALUES (1,'ACTIVO'),(2,'INACTIVO'),(3,'ELIMINADO');
/*!40000 ALTER TABLE `estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libros`
--

DROP TABLE IF EXISTS `libros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libros` (
  `libro_id` int(11) NOT NULL AUTO_INCREMENT,
  `isbn` varchar(15) DEFAULT NULL,
  `url_portada` varchar(250) DEFAULT NULL,
  `libro_nom` varchar(250) DEFAULT NULL,
  `descripcion` varchar(250) DEFAULT NULL,
  `anio_publicacion` varchar(4) DEFAULT NULL,
  `edicion` varchar(100) DEFAULT NULL,
  `existencias` int(11) DEFAULT NULL,
  `categoria_id` int(11) DEFAULT NULL,
  `editorial_id` int(11) DEFAULT NULL,
  `autor_id` int(11) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `usuario_creacion_id` int(11) DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  `usuario_actualizacion_id` int(11) DEFAULT NULL,
  `estado_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`libro_id`),
  KEY `categoria_id` (`categoria_id`),
  KEY `editorial_id` (`editorial_id`),
  KEY `autor_id` (`autor_id`),
  KEY `usuario_creacion_id` (`usuario_creacion_id`),
  KEY `usuario_actualizacion_id` (`usuario_actualizacion_id`),
  KEY `estado_id` (`estado_id`),
  CONSTRAINT `libros_ibfk_1` FOREIGN KEY (`categoria_id`) REFERENCES `categorias` (`categoria_id`),
  CONSTRAINT `libros_ibfk_2` FOREIGN KEY (`editorial_id`) REFERENCES `editoriales` (`editorial_id`),
  CONSTRAINT `libros_ibfk_3` FOREIGN KEY (`autor_id`) REFERENCES `autores` (`autor_id`),
  CONSTRAINT `libros_ibfk_4` FOREIGN KEY (`usuario_creacion_id`) REFERENCES `usuarios` (`usuario_id`),
  CONSTRAINT `libros_ibfk_5` FOREIGN KEY (`usuario_actualizacion_id`) REFERENCES `usuarios` (`usuario_id`),
  CONSTRAINT `libros_ibfk_6` FOREIGN KEY (`estado_id`) REFERENCES `estado` (`estado_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libros`
--

LOCK TABLES `libros` WRITE;
/*!40000 ALTER TABLE `libros` DISABLE KEYS */;
INSERT INTO `libros` VALUES (1,'9780140449136','https://example.com/portadas/odisea.jpg','La Odisea','Épica griega de Homero.','2003','1ra',5,1,6,1,'2025-05-14 04:22:06',1,'2025-06-24 22:19:57',1,1),(2,'9788437604947','https://example.com/portadas/quijote.jpg','Don Quijote de la Mancha','Obra clásica de Cervantes.','2005','2da',8,2,5,2,'2025-05-14 04:22:06',1,'2025-06-24 22:19:37',1,1),(3,'9788491050487','https://example.com/portadas/1984.jpg','1984','Distopía de George Orwell.','2016','3ra',10,1,2,3,'2025-05-14 04:22:06',1,'2025-06-27 23:03:24',1,1),(4,'9780307387899','https://example.com/portadas/cien_anos.jpg','Cien años de soledad','Obra maestra de Gabriel García Márquez.','2014','5ta',6,1,3,4,'2025-05-14 04:22:06',1,'2025-05-14 04:22:06',1,1),(5,'9780061122415','https://example.com/portadas/matar_ruisenor.jpg','Matar a un ruiseñor','Novela de Harper Lee.','2006','1ra',4,2,4,5,'2025-05-14 04:22:06',1,'2025-05-14 04:22:06',1,1),(6,'9788423343050','https://example.com/portadas/el_alquimista.jpg','El alquimista','Novela de Paulo Coelho.','2010','6ta',7,2,5,6,'2025-05-14 04:22:06',1,'2025-05-14 04:22:06',1,1),(7,'9788498387087','https://example.com/portadas/hp_piedra.jpg','Harry Potter y la piedra filosofal','Primera entrega de la saga.','2009','7ma',12,7,6,7,'2025-05-14 04:22:06',1,'2025-05-14 04:22:06',1,1),(8,'9788420674170','https://example.com/portadas/crimen_castigo.jpg','Crimen y castigo','Novela de Dostoievski.','2007','4ta',5,1,7,8,'2025-05-14 04:22:06',1,'2025-05-14 04:22:06',1,1),(9,'9789877383614','https://example.com/portadas/sapiens.jpg','Sapiens','Breve historia de la humanidad.','2018','2da',9,3,8,9,'2025-05-14 04:22:06',1,'2025-05-14 04:22:06',1,1),(10,'9789501246456','https://example.com/portadas/el_principito.jpg','El Principito','Obra de Antoine de Saint-Exupéry.','2013','10ma',15,1,8,10,'2025-05-14 04:22:06',1,'2025-06-24 22:20:34',1,1),(11,'1234567891','','vida y obra de goku','un libro con goku','2025','1era',50,9,6,4,'2025-06-10 01:09:26',1,'2025-06-29 13:39:27',1,2),(12,'9780345402882','','Jurassic Park the lost world','secuela de la afamada obra jurasicc park','1997','1era',50,1,3,2,'2025-06-19 14:34:13',1,NULL,NULL,1);
/*!40000 ALTER TABLE `libros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona`
--

DROP TABLE IF EXISTS `persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persona` (
  `persona_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(50) DEFAULT NULL,
  `apellidos` varchar(50) DEFAULT NULL,
  `num_contacto` int(11) DEFAULT NULL,
  `correo` varchar(50) DEFAULT NULL,
  `dni` varchar(8) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `usuario_creacion_id` int(11) DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  `usuario_actualizacion_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`persona_id`),
  UNIQUE KEY `dni` (`dni`),
  KEY `fk_persona_creacion` (`usuario_creacion_id`),
  KEY `fk_persona_actualizacion` (`usuario_actualizacion_id`),
  CONSTRAINT `fk_persona_actualizacion` FOREIGN KEY (`usuario_actualizacion_id`) REFERENCES `usuarios` (`usuario_id`),
  CONSTRAINT `fk_persona_creacion` FOREIGN KEY (`usuario_creacion_id`) REFERENCES `usuarios` (`usuario_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona`
--

LOCK TABLES `persona` WRITE;
/*!40000 ALTER TABLE `persona` DISABLE KEYS */;
INSERT INTO `persona` VALUES (1,'Juan','Pérez',987654321,'juan.perez@example.com','12345678','Av. Siempre Viva 123','2025-05-13 01:35:57',NULL,'2025-05-13 01:35:57',NULL),(2,'María','Gómez',912345678,'maria.gomez@example.com','23456789','Calle Falsa 456','2025-05-13 01:35:57',NULL,'2025-05-13 01:35:57',NULL),(3,'Luis','Ramírez',923456789,'luis.ramirez@example.com','34567890','Jr. Las Flores 789','2025-05-13 01:35:57',NULL,'2025-05-13 01:35:57',NULL),(4,'Ana','Fernández',934567890,'ana.fernandez@example.com','45678901','Pasaje Los Andes 321','2025-05-13 01:35:57',NULL,'2025-05-13 01:35:57',NULL),(5,'Carlos','López',945678901,'carlos.lopez@example.com','56789012','Av. Los Incas 654','2025-05-13 01:35:57',NULL,'2025-05-13 01:35:57',NULL),(6,'Lucía','Mendoza',956789012,'lucia.mendoza@example.com','67890123','Calle Libertad 789','2025-05-13 01:35:57',NULL,'2025-05-13 01:35:57',NULL),(7,'Pedro','Castro',967890123,'pedro.castro@example.com','78901234','Jr. Amazonas 101','2025-05-13 01:35:57',NULL,'2025-05-13 01:35:57',NULL),(8,'Laura','Silva',978901234,'laura.silva@example.com','89012345','Av. Grau 202','2025-05-13 01:35:57',NULL,'2025-05-13 01:35:57',NULL),(9,'Miguel','Torres',989012345,'miguel.torres@example.com','90123456','Calle Lima 303','2025-05-13 01:35:57',NULL,'2025-05-13 01:35:57',NULL),(10,'Sofía','Ríos',999123456,'sofia.rios@example.com','01234567','Jr. Cusco 404','2025-05-13 01:35:57',NULL,'2025-05-13 01:35:57',NULL),(11,'Jean Franco','Reategui',965993321,'jeanreategui@example.com','75152868','Av. Siempre Viva 123','2025-05-13 01:38:18',NULL,'2025-05-13 01:38:18',NULL),(13,'Juan Pablo','Ruelas Rojas',965993321,'pablito@gmail.com','78598324','su jato',NULL,NULL,NULL,NULL),(14,'Jose Luis','Carihuasairo Rayo',965993321,'jose@gmail.com','45678923','su casa tambien',NULL,NULL,NULL,NULL),(15,'Kelvin','Huaman Achaca2',965993321,'kelvincito@gmail.com','56781232','su casita',NULL,NULL,NULL,NULL),(16,'paul christian','lopez ruiz',95324587,'paultubebita@gmai.com','98784532','you casa p',NULL,NULL,NULL,NULL),(17,'mario','broll',895645124,'marioborss@gmail.com','89562321','mushroom kingdom',NULL,NULL,NULL,NULL),(18,'luigi','bross go',987546123,'luigibross@gmail.com','23458965','mushroom kingdom ',NULL,NULL,NULL,NULL),(19,'princess','peach',789456123,'darkprincess@gmail.com','23546598','mushroom kingdom ',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prestamos`
--

DROP TABLE IF EXISTS `prestamos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prestamos` (
  `prestamo_id` int(11) NOT NULL AUTO_INCREMENT,
  `libro_id` int(11) DEFAULT NULL,
  `usuario_solicita_prestamo` int(11) DEFAULT NULL,
  `usuario_aprueba_prestamo` int(11) DEFAULT NULL,
  `fecha_solicitud_prestamo` datetime DEFAULT NULL,
  `fecha_devolucion_prestamo` datetime DEFAULT NULL,
  `prestamo_estado_id` int(11) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `usuario_creacion_id` int(11) DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  `usuario_actualizacion_id` int(11) DEFAULT NULL,
  `estado_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`prestamo_id`),
  KEY `fk_prestamo_libro` (`libro_id`),
  KEY `fk_prestamo_usuario_solicita` (`usuario_solicita_prestamo`),
  KEY `fk_prestamo_usuario_aprueba` (`usuario_aprueba_prestamo`),
  KEY `fk_prestamo_estado` (`prestamo_estado_id`),
  KEY `fk_prestamo_creacion` (`usuario_creacion_id`),
  KEY `fk_prestamo_actualizacion` (`usuario_actualizacion_id`),
  KEY `estado_id` (`estado_id`),
  CONSTRAINT `fk_prestamo_actualizacion` FOREIGN KEY (`usuario_actualizacion_id`) REFERENCES `usuarios` (`usuario_id`),
  CONSTRAINT `fk_prestamo_creacion` FOREIGN KEY (`usuario_creacion_id`) REFERENCES `usuarios` (`usuario_id`),
  CONSTRAINT `fk_prestamo_estado` FOREIGN KEY (`prestamo_estado_id`) REFERENCES `prestamos_estado` (`prestamo_estado_id`),
  CONSTRAINT `fk_prestamo_libro` FOREIGN KEY (`libro_id`) REFERENCES `libros` (`libro_id`),
  CONSTRAINT `fk_prestamo_usuario_aprueba` FOREIGN KEY (`usuario_aprueba_prestamo`) REFERENCES `usuarios` (`usuario_id`),
  CONSTRAINT `fk_prestamo_usuario_solicita` FOREIGN KEY (`usuario_solicita_prestamo`) REFERENCES `usuarios` (`usuario_id`),
  CONSTRAINT `prestamos_ibfk_1` FOREIGN KEY (`estado_id`) REFERENCES `estado` (`estado_id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prestamos`
--

LOCK TABLES `prestamos` WRITE;
/*!40000 ALTER TABLE `prestamos` DISABLE KEYS */;
INSERT INTO `prestamos` VALUES (21,1,1,1,'2025-05-01 10:00:00','2025-05-08 10:00:00',1,'2025-05-01 10:00:00',1,'2025-05-01 10:00:00',1,1),(22,2,1,1,'2025-05-02 11:30:00','2025-05-09 11:30:00',1,'2025-05-02 11:30:00',1,'2025-05-02 11:30:00',1,1),(23,3,1,1,'2025-05-03 09:00:00',NULL,2,'2025-05-03 09:00:00',1,'2025-05-03 09:00:00',1,1),(24,4,1,1,'2025-05-04 14:15:00',NULL,2,'2025-05-04 14:15:00',1,'2025-05-04 14:15:00',1,1),(25,5,1,1,'2025-04-28 13:45:00','2025-05-05 13:45:00',1,'2025-04-28 13:45:00',1,'2025-04-28 13:45:00',1,1),(26,6,1,1,'2025-05-05 08:20:00','2025-05-12 08:20:00',1,'2025-05-05 08:20:00',1,'2025-05-05 08:20:00',1,1),(27,7,1,1,'2025-05-06 16:10:00',NULL,2,'2025-05-06 16:10:00',1,'2025-05-06 16:10:00',1,1),(28,8,1,1,'2025-05-07 17:00:00','2025-05-14 17:00:00',1,'2025-05-07 17:00:00',1,'2025-06-28 16:07:30',1,1),(29,9,1,1,'2025-05-08 10:10:00',NULL,2,'2025-05-08 10:10:00',1,'2025-05-08 10:10:00',1,1),(30,10,1,1,'2025-05-09 12:00:00',NULL,2,'2025-05-09 12:00:00',1,'2025-05-09 12:00:00',1,1),(34,1,3,1,'2025-06-09 10:30:00','2025-06-16 17:00:00',1,'2025-06-19 16:35:19',1,NULL,NULL,1),(36,4,1,1,'2025-06-19 21:57:35','2025-06-26 21:57:35',1,'2025-06-19 16:57:35',1,'2025-06-27 23:03:14',1,1),(37,4,4,1,'2025-06-28 20:53:13','2025-07-05 20:53:13',1,'2025-06-28 15:53:14',1,'2025-06-29 13:38:58',1,2);
/*!40000 ALTER TABLE `prestamos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prestamos_estado`
--

DROP TABLE IF EXISTS `prestamos_estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prestamos_estado` (
  `prestamo_estado_id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`prestamo_estado_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prestamos_estado`
--

LOCK TABLES `prestamos_estado` WRITE;
/*!40000 ALTER TABLE `prestamos_estado` DISABLE KEYS */;
INSERT INTO `prestamos_estado` VALUES (1,'APROBADO'),(2,'SOLICITADO'),(3,'DEVUELTO');
/*!40000 ALTER TABLE `prestamos_estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `record_usuarios`
--

DROP TABLE IF EXISTS `record_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `record_usuarios` (
  `record_usuario_id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(255) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `usuario_creacion_id` int(11) DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  `usuario_actualizacion_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`record_usuario_id`),
  KEY `fk_record_creacion` (`usuario_creacion_id`),
  KEY `fk_record_actualizacion` (`usuario_actualizacion_id`),
  CONSTRAINT `fk_record_actualizacion` FOREIGN KEY (`usuario_actualizacion_id`) REFERENCES `usuarios` (`usuario_id`),
  CONSTRAINT `fk_record_creacion` FOREIGN KEY (`usuario_creacion_id`) REFERENCES `usuarios` (`usuario_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `record_usuarios`
--

LOCK TABLES `record_usuarios` WRITE;
/*!40000 ALTER TABLE `record_usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `record_usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `usuario_id` int(11) NOT NULL AUTO_INCREMENT,
  `usu_nom` varchar(50) DEFAULT NULL,
  `usu_pass` varchar(200) DEFAULT NULL,
  `persona_id` int(11) DEFAULT NULL,
  `usuario_tipo_id` int(11) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `usuario_creacion_id` int(11) DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  `usuario_actualizacion_id` int(11) DEFAULT NULL,
  `estado_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`usuario_id`),
  KEY `fk_usuarios_persona` (`persona_id`),
  KEY `fk_usuarios_tipo` (`usuario_tipo_id`),
  KEY `fk_usuarios_creacion` (`usuario_creacion_id`),
  KEY `fk_usuarios_actualizacion` (`usuario_actualizacion_id`),
  KEY `estado_id` (`estado_id`),
  CONSTRAINT `fk_usuarios_actualizacion` FOREIGN KEY (`usuario_actualizacion_id`) REFERENCES `usuarios` (`usuario_id`),
  CONSTRAINT `fk_usuarios_creacion` FOREIGN KEY (`usuario_creacion_id`) REFERENCES `usuarios` (`usuario_id`),
  CONSTRAINT `fk_usuarios_persona` FOREIGN KEY (`persona_id`) REFERENCES `persona` (`persona_id`),
  CONSTRAINT `fk_usuarios_tipo` FOREIGN KEY (`usuario_tipo_id`) REFERENCES `usuarios_tipo` (`usuario_tipo_id`),
  CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`estado_id`) REFERENCES `estado` (`estado_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'jreategui','scrypt:32768:8:1$VDvbDaoPIJoUBvY3$c09d542acd1868700aa83a9e0dbc106e3564c5f5d3ad6bfdac0d5fa2cde205622bef5bae72237fa947dfd7360d86ae3d246c473d1c052d461f4e153d7d833c42',11,1,NULL,NULL,NULL,NULL,1),(3,'jruelasrojas','scrypt:32768:8:1$8SvtCMYU6F4YBKYq$03c2c8dfc719a40092601b5f34eeb2152bfa712dc261743e7ff632aa38d8f4951bddfc924796660335ae2a6601a485edb59750634bdaca4440fafd78ca03a6b8',13,1,NULL,NULL,NULL,NULL,2),(4,'jcarihuasairorayo','scrypt:32768:8:1$7wdH0ZCfJTDxpWPu$2592202ed3947d0c1ac9f32bd9d9ed358f2f784763705f7cad82a08bd30d66920776fcfa26ab2bc3ce709d117205414868ca9c5cba142987f46b9dfbf6bd2a31',14,1,NULL,NULL,NULL,NULL,1),(5,'khuamanachaca','scrypt:32768:8:1$qcH7bdVRtTSRT94m$d3f5abda2be505db44997bb9a58bc97e99a39dc657127cd66e2ea205c8344b9efe1bdbfe79b9736dbbe34b299d05a26216a7331dcc90d4c1cf9b1a7e293a4f45',15,3,NULL,NULL,'2025-06-27 01:49:27',1,1),(6,'plopezruiz','scrypt:32768:8:1$TwQDz6bWwak986pd$6ec6ca213bdfe2b2b63c4189b245a54f7a68a5be2dce18bc8593aae176c875fc48d23bed4934f5cf43d1a8acd0dc103153bedbc64e7aa782df97b388ce036408',16,3,NULL,NULL,NULL,NULL,1),(7,'mbross','scrypt:32768:8:1$jt0eiTuVXT66mW3I$140f4596874ac943205be0a5e2f7981149686b1d6032939c65e83737b3ffd7978881ee85136d979884253bd904ff51f30e7b436e94d8792f9e9bda8ea9bff8c4',17,1,NULL,NULL,'2025-06-27 01:50:03',1,2),(8,'lbross','scrypt:32768:8:1$4FYR9lgr3uzBY34K$2a9595de804ede18fe08c3abb2c90f8c250c083eb61797e7d33826f5303c74f0f94dab4caf719ebf8086b377858d7ea7964bfccde36da5942f5283f90b7517ee',18,1,NULL,NULL,'2025-06-27 01:41:41',1,2),(9,'ppeach','scrypt:32768:8:1$kvzojndMEkb2Yen8$ccd5de917b2327dfb953ece1692347ee8b13b2ee28ddb1462d7a1dac2b9e18a5de366ab364598ef97ec42eefbb7254e75801c11f4f44ba450a64e619154ce72a',19,NULL,NULL,NULL,'2025-06-25 01:20:27',1,2);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_tipo`
--

DROP TABLE IF EXISTS `usuarios_tipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_tipo` (
  `usuario_tipo_id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_nom` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`usuario_tipo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_tipo`
--

LOCK TABLES `usuarios_tipo` WRITE;
/*!40000 ALTER TABLE `usuarios_tipo` DISABLE KEYS */;
INSERT INTO `usuarios_tipo` VALUES (1,'ADMINISTRADOR'),(3,'TRABAJADOR');
/*!40000 ALTER TABLE `usuarios_tipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'db_biblioteca_v1'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-29 23:08:47
