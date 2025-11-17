-- Active: 1763327576084@@127.0.0.1@3306@mysql
-- Active: 1763327576084@@127.0.0.1@3306@tarea2
-- schema-tarea2.sql
DROP SCHEMA IF EXISTS `tarea2`;
CREATE SCHEMA IF NOT EXISTS `tarea2` DEFAULT CHARACTER SET utf8;
USE `tarea2`;

CREATE TABLE IF NOT EXISTS `region` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `comuna` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  `region_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comuna_region1_idx` (`region_id` ASC),
  CONSTRAINT `fk_comuna_region1`
    FOREIGN KEY (`region_id`)
    REFERENCES `region` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `aviso_adopcion` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fecha_ingreso` DATETIME NOT NULL,
  `comuna_id` INT NOT NULL,
  `sector` VARCHAR(100) NULL,
  `nombre` VARCHAR(200) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `celular` VARCHAR(15) NULL,
  `tipo` ENUM('gato', 'perro') NOT NULL,
  `cantidad` INT NOT NULL,
  `edad` INT NOT NULL,
  `unidad_medida` ENUM('a', 'm') NOT NULL,
  `fecha_entrega` DATETIME NOT NULL,
  `descripcion` TEXT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_aviso_comuna1_idx` (`comuna_id` ASC),
  CONSTRAINT `fk_aviso_comuna1`
    FOREIGN KEY (`comuna_id`)
    REFERENCES `comuna` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE=InnoDB;

-- tabla nota (según enunciado)
CREATE TABLE IF NOT EXISTS `nota` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `aviso_id` INT NOT NULL,
  `nota` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_nota_aviso1_idx` (`aviso_id` ASC),
  CONSTRAINT `fk_nota_aviso1`
    FOREIGN KEY (`aviso_id`)
    REFERENCES `aviso_adopcion` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE=InnoDB;
