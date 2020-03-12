-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema sqlproject
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sqlproject
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sqlproject` DEFAULT CHARACTER SET utf8 ;
USE `sqlproject` ;

-- -----------------------------------------------------
-- Table `sqlproject`.`USER`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sqlproject`.`USER` (
  `USERNAME` VARCHAR(45) NOT NULL,
  `PASSWORD` VARCHAR(45) NOT NULL,
  `U_ID` CHAR(5) NOT NULL,
  PRIMARY KEY (`U_ID`),
  UNIQUE INDEX `U_ID_UNIQUE` (`U_ID` ASC) VISIBLE,
  UNIQUE INDEX `USERNAME_UNIQUE` (`USERNAME` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sqlproject`.`QUALITY_INDEX`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sqlproject`.`QUALITY_INDEX` (
  `QUALITY_OF_SLEEP (1-10)` INT NULL,
  `OVERALL_HAPPINESS (1-10)` INT NULL,
  `COMMENT` VARCHAR(45) NULL,
  `DATE` DATE NOT NULL,
  PRIMARY KEY (`DATE`),
  UNIQUE INDEX `DATE_UNIQUE` (`DATE` ASC) VISIBLE,
  CONSTRAINT `DATE`
    FOREIGN KEY (`DATE`)
    REFERENCES `sqlproject`.`DAILY_ROUTINE` (`DATE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sqlproject`.`PROJECT/SELF_LEARNING`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sqlproject`.`PROJECT/SELF_LEARNING` (
  `PROJECT_ID` INT NOT NULL,
  `PROJECT_NAME` VARCHAR(45) NOT NULL,
  `HOURS_SPENT` DECIMAL(24) NULL,
  PRIMARY KEY (`PROJECT_ID`),
  UNIQUE INDEX `PROJECT_ID_UNIQUE` (`PROJECT_ID` ASC) VISIBLE,
  CONSTRAINT `PROJECT_ID`
    FOREIGN KEY (`PROJECT_ID`)
    REFERENCES `sqlproject`.`DAILY_ROUTINE` (`PROJECT_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sqlproject`.`DAILY_ROUTINE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sqlproject`.`DAILY_ROUTINE` (
  `DATE` DATE NOT NULL,
  `HOURS_OF_SLEEP` DECIMAL(24) NULL,
  `CLASSES_ATTENDED (hrs)` DECIMAL(24) NULL,
  `HOBBIES (hrs)` DECIMAL(24) NULL,
  `FITNESS (hrs)` DECIMAL(24) NULL,
  `PROJECT_ID` INT NOT NULL,
  PRIMARY KEY (`DATE`),
  UNIQUE INDEX `DATE_UNIQUE` (`DATE` ASC) VISIBLE,
  UNIQUE INDEX `PROJECT_ID_UNIQUE` (`PROJECT_ID` ASC) VISIBLE,
  CONSTRAINT `DATE`
    FOREIGN KEY (`DATE`)
    REFERENCES `sqlproject`.`QUALITY_INDEX` (`DATE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `PROJECT_ID`
    FOREIGN KEY (`PROJECT_ID`)
    REFERENCES `sqlproject`.`PROJECT/SELF_LEARNING` (`PROJECT_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
