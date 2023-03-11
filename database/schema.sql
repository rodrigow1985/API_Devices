USE `db_home-server`;

CREATE TABLE IF NOT EXISTS `devices` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key',
  `name` varchar(200) NOT NULL COMMENT 'Device name',
  `description` text NULL COMMENT 'Device description',
  `code` varchar(20) NOT NULL COMMENT 'Device code',
  `image` varchar(200) NULL COMMENT 'url to the device image',
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  FULLTEXT KEY `description` (`description`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Devices table';

INSERT INTO `devices` (`id`, `name`, `description`, `code`, `image`, `created_at`, `updated_at`) 
VALUES (NULL, 'device1', 'device1 description', '0001', 'http://url_image1', 
'2023-03-09 02:57:13.000000', '2023-03-09 02:57:13.000000');

/* Stored Procedures */

CREATE DEFINER=`rodrigo`@`%` PROCEDURE `add_device`(IN `name` VARCHAR(200), IN `description` TEXT, IN `code` VARCHAR(20), IN `image` VARCHAR(200), IN `created_at` DATETIME, IN `updated_at` DATETIME, OUT `id` INT) COMMENT 'Add a new device' NOT DETERMINISTIC CONTAINS SQL SQL SECURITY DEFINER BEGIN INSERT INTO `devices` (`id`, `name`, `description`, `code`, `image`, `created_at`, `updated_at`) VALUES (`id`, `name`, `description`, `code`, `image`, `created_at`, `updated_at`); SET `id` = LAST_INSERT_ID(); END
CREATE PROCEDURE `select_devices`() COMMENT 'Select all from devices' NOT DETERMINISTIC CONTAINS SQL SQL SECURITY DEFINER SELECT * FROM `devices` 
CREATE PROCEDURE `select_divice_by_id` (IN `id` INT) COMMENT 'Select a device by id' NOT DETERMINISTIC CONTAINS SQL SQL SECURITY DEFINER SELECT * FROM `devices` WHERE `devices`.`id` = `id` 

