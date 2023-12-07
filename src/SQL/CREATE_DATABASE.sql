-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema tepuy_delivery
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tepuy_delivery
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tepuy_delivery` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `tepuy_delivery` ;

-- -----------------------------------------------------
-- Table `tepuy_delivery`.`brand`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tepuy_delivery`.`brand` (
  `brand_id` INT NOT NULL,
  `brand` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`brand_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `tepuy_delivery`.`channel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tepuy_delivery`.`channel` (
  `channel_id` INT NOT NULL,
  `channel` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`channel_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `tepuy_delivery`.`delivery_timing`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tepuy_delivery`.`delivery_timing` (
  `delivery_timing_id` INT NOT NULL,
  `delivery_timing` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`delivery_timing_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `tepuy_delivery`.`menu`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tepuy_delivery`.`menu` (
  `item_id` INT NOT NULL,
  `item` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`item_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `tepuy_delivery`.`location`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tepuy_delivery`.`location` (
  `location_id` INT NOT NULL,
  `location` VARCHAR(50) NULL DEFAULT NULL,
  `brand_direct` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`location_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `tepuy_delivery`.`status`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tepuy_delivery`.`status` (
  `status_id` INT NOT NULL,
  `status` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`status_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `tepuy_delivery`.`order_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tepuy_delivery`.`order_type` (
  `order_type_id` INT NOT NULL,
  `order_type` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`order_type_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `tepuy_delivery`.`software`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tepuy_delivery`.`software` (
  `software_id` INT NOT NULL,
  `software` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`software_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `tepuy_delivery`.`order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tepuy_delivery`.`order` (
  `order_id` INT NOT NULL,
  `order_id_software` VARCHAR(50) NULL DEFAULT NULL,
  `created_datetime` VARCHAR(50) NULL DEFAULT NULL,
  `quantity` FLOAT NULL DEFAULT NULL,
  `subtotal` FLOAT NULL DEFAULT NULL,
  `tip` FLOAT NULL DEFAULT NULL,
  `driver_tip` INT NULL DEFAULT NULL,
  `discount` FLOAT NULL DEFAULT NULL,
  `total` FLOAT NULL DEFAULT NULL,
  `payment_method` VARCHAR(50) NULL DEFAULT NULL,
  `vat` FLOAT NULL DEFAULT NULL,
  `location_id` INT NULL DEFAULT NULL,
  `channel_id` INT NULL DEFAULT NULL,
  `status_id` INT NULL DEFAULT NULL,
  `order_type_id` INT NULL DEFAULT NULL,
  `software_id` INT NULL DEFAULT NULL,
  `delivery_timing_id` INT NULL DEFAULT NULL,
  `delivery_rate` DECIMAL(10,2) NULL DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  INDEX `location_id` (`location_id` ASC) VISIBLE,
  INDEX `channel_id` (`channel_id` ASC) VISIBLE,
  INDEX `status_id` (`status_id` ASC) VISIBLE,
  INDEX `order_type_id` (`order_type_id` ASC) VISIBLE,
  INDEX `software_id` (`software_id` ASC) VISIBLE,
  INDEX `delivery_timing_id` (`delivery_timing_id` ASC) VISIBLE,
  CONSTRAINT `order_ibfk_1`
    FOREIGN KEY (`location_id`)
    REFERENCES `tepuy_delivery`.`location` (`location_id`),
  CONSTRAINT `order_ibfk_2`
    FOREIGN KEY (`channel_id`)
    REFERENCES `tepuy_delivery`.`channel` (`channel_id`),
  CONSTRAINT `order_ibfk_3`
    FOREIGN KEY (`status_id`)
    REFERENCES `tepuy_delivery`.`status` (`status_id`),
  CONSTRAINT `order_ibfk_4`
    FOREIGN KEY (`order_type_id`)
    REFERENCES `tepuy_delivery`.`order_type` (`order_type_id`),
  CONSTRAINT `order_ibfk_5`
    FOREIGN KEY (`software_id`)
    REFERENCES `tepuy_delivery`.`software` (`software_id`),
  CONSTRAINT `order_ibfk_6`
    FOREIGN KEY (`delivery_timing_id`)
    REFERENCES `tepuy_delivery`.`delivery_timing` (`delivery_timing_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `tepuy_delivery`.`item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tepuy_delivery`.`item` (
  `order_id` INT NOT NULL,
  `item_id` INT NOT NULL,
  `item` VARCHAR(50) NULL DEFAULT NULL,
  `quantity` INT NULL DEFAULT NULL,
  `price` FLOAT NULL DEFAULT NULL,
  `total_item` FLOAT NULL DEFAULT NULL,
  `service_fee` FLOAT NULL DEFAULT NULL,
  `order_id_software` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`item_id`, `order_id`),
  INDEX `order_id` (`order_id` ASC) VISIBLE,
  CONSTRAINT `item_ibfk_1`
    FOREIGN KEY (`item_id`)
    REFERENCES `tepuy_delivery`.`menu` (`item_id`),
  CONSTRAINT `item_ibfk_2`
    FOREIGN KEY (`order_id`)
    REFERENCES `tepuy_delivery`.`order` (`order_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `tepuy_delivery`.`location_brand`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tepuy_delivery`.`location_brand` (
  `location_id` INT NOT NULL,
  `brand_id` INT NOT NULL,
  PRIMARY KEY (`location_id`, `brand_id`),
  INDEX `brand_id` (`brand_id` ASC) VISIBLE,
  CONSTRAINT `location_brand_ibfk_1`
    FOREIGN KEY (`location_id`)
    REFERENCES `tepuy_delivery`.`location` (`location_id`),
  CONSTRAINT `location_brand_ibfk_2`
    FOREIGN KEY (`brand_id`)
    REFERENCES `tepuy_delivery`.`brand` (`brand_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
