-- --------------------------------------------------------
-- Хост:                         127.0.0.1
-- Версия сервера:               5.5.53 - MySQL Community Server (GPL)
-- Операционная система:         Win32
-- HeidiSQL Версия:              9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Дамп структуры базы данных projects
CREATE DATABASE IF NOT EXISTS `projects` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `projects`;

-- Дамп структуры для таблица projects.employees
CREATE TABLE IF NOT EXISTS `employees` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Дамп данных таблицы projects.employees: 1 rows
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` (`id`, `name`, `description`) VALUES
	(1, 'Marchenko', 'added by user');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;

-- Дамп структуры для таблица projects.employers
CREATE TABLE IF NOT EXISTS `employers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT '0',
  `description` varchar(50) DEFAULT '0',
  KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Дамп данных таблицы projects.employers: 3 rows
/*!40000 ALTER TABLE `employers` DISABLE KEYS */;
INSERT INTO `employers` (`id`, `name`, `description`) VALUES
	(1, 'Ihnat', 'added by user'),
	(2, 'Petrashenko', 'added by user'),
	(3, 'Vadim', 'added by user');
/*!40000 ALTER TABLE `employers` ENABLE KEYS */;

-- Дамп структуры для таблица projects.languages
CREATE TABLE IF NOT EXISTS `languages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '0',
  `description` varchar(50) NOT NULL DEFAULT '0',
  KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Дамп данных таблицы projects.languages: 2 rows
/*!40000 ALTER TABLE `languages` DISABLE KEYS */;
INSERT INTO `languages` (`id`, `name`, `description`) VALUES
	(1, 'Php', 'added from file'),
	(2, 'Python', 'added from file');
/*!40000 ALTER TABLE `languages` ENABLE KEYS */;

-- Дамп структуры для таблица projects.projects
CREATE TABLE IF NOT EXISTS `projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Дамп данных таблицы projects.projects: 3 rows
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` (`id`, `name`, `description`) VALUES
	(1, 'jeweldreams', 'added by user'),
	(2, 'lab2db', 'added by user'),
	(3, 'fullcontrol', 'added by user');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;

-- Дамп структуры для таблица projects.tasks
CREATE TABLE IF NOT EXISTS `tasks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `project_id` varchar(50) DEFAULT NULL,
  `employee_id` varchar(50) DEFAULT NULL,
  `employer_id` varchar(50) DEFAULT NULL,
  `language_id` varchar(50) DEFAULT NULL,
  `difficulty` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `description` varchar(191) DEFAULT NULL,
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- Дамп данных таблицы projects.tasks: ~7 rows (приблизительно)
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` (`id`, `name`, `project_id`, `employee_id`, `employer_id`, `language_id`, `difficulty`, `date`, `description`) VALUES
	(9, 'create client interface template', 'fullcontrol', 'Marchenko', 'Vadim', 'PHP', 1, '09/11/2017', 'Create template for CRUD system'),
	(10, 'sdjsadjk', 'fullcontrol', 'Marchenko', 'Ihnat', 'Php', 2, '22/11/2222', 'sghdsahj'),
	(11, 'create template', 'lab2db', 'Marchenko', 'Petrashenko', 'Python', 1, '09/11/2017', 'Create template for CRUD system'),
	(12, 'create client interface template', 'fullcontrol', 'Marchenko', 'Vadim', 'PHP', 1, '09/11/2017', 'Create template for CRUD system'),
	(13, 'create selling system', 'jeweldreams', 'Marchenko', 'Ihnat', 'PHP', 2, '09/11/2017', 'table Sells ,create check'),
	(14, 'create template', 'lab2db', 'Marchenko', 'Petrashenko', 'Python', 1, '09/11/2017', 'Create template for CRUD system'),
	(15, 'create client interface template', 'fullcontrol', 'Marchenko', 'Vadim', 'PHP', 1, '09/11/2017', 'Create template for CRUD system');
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
