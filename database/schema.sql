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

CREATE PROCEDURE `add_device`(IN `name` VARCHAR(200), IN `description` TEXT, IN `code` VARCHAR(20), IN `image` VARCHAR(200), IN `created_at` DATETIME, IN `updated_at` DATETIME) COMMENT 'Add a new device' NOT DETERMINISTIC CONTAINS SQL SQL SECURITY DEFINER INSERT INTO `devices` (`id`, `name`, `description`, `code`, `image`, `created_at`, `updated_at`) VALUES (`id`, `name`, `description`, `code`, `image`, `created_at`, `updated_at`);



