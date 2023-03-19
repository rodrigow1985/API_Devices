USE `db_home-server`;

SET GLOBAL time_zone = 'America/Argentina/Buenos_Aires';

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

CREATE DEFINER=`rodrigo`@`%` PROCEDURE `add_device`(IN `name` VARCHAR(200), IN `description` TEXT, IN `code` VARCHAR(20), IN `image` VARCHAR(200), OUT `id` INT) COMMENT 'Add a new device' NOT DETERMINISTIC CONTAINS SQL SQL SECURITY DEFINER BEGIN INSERT INTO `devices` (`id`, `name`, `description`, `code`, `image`, `created_at`, `updated_at`) VALUES (`id`, `name`, `description`, `code`, `image`, now(), now()); SET `id` = LAST_INSERT_ID(); END
CREATE PROCEDURE `select_devices`() COMMENT 'Select all from devices' NOT DETERMINISTIC CONTAINS SQL SQL SECURITY DEFINER SELECT * FROM `devices` 
CREATE PROCEDURE `select_divice_by_id` (IN `id` INT) COMMENT 'Select a device by id' NOT DETERMINISTIC CONTAINS SQL SQL SECURITY DEFINER SELECT * FROM `devices` WHERE `devices`.`id` = `id` 
CREATE PROCEDURE `update_device`(IN `id` INT, IN `name` VARCHAR(200), IN `description` TEXT, IN `code` VARCHAR(20), IN `image` VARCHAR(200), OUT `updated_at` DATETIME) COMMENT 'Update a device' NOT DETERMINISTIC CONTAINS SQL SQL SECURITY DEFINER BEGIN UPDATE `devices` SET `devices`.`name` = `name`, `devices`.`description` = `description`, `devices`.`code` = `code`, `devices`.`image` = `image`, `devices`.`updated_at` = now() WHERE `devices`.`id` = `id`; SET `updated_at` = now(); END
CREATE DEFINER=`root`@`%` PROCEDURE `delete_device`(IN `id` INT, OUT `deleted_at` DATETIME) NOT DETERMINISTIC CONTAINS SQL SQL SECURITY DEFINER BEGIN DELETE FROM `devices` WHERE `devices`.`id` = `id`; SET `deleted_at` = NOW(); END