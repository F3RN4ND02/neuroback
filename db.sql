-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema new_schema1
-- -----------------------------------------------------
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`paises`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`paises` ;

CREATE TABLE IF NOT EXISTS `mydb`.`paises` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `codigo` VARCHAR(2) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `codigo_UNIQUE` (`codigo` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`estados`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`estados` ;

CREATE TABLE IF NOT EXISTS `mydb`.`estados` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `paises_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_estados_paises1_idx` (`paises_id` ASC) ,
  CONSTRAINT `fk_estados_paises1`
    FOREIGN KEY (`paises_id`)
    REFERENCES `mydb`.`paises` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`municipios`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`municipios` ;

CREATE TABLE IF NOT EXISTS `mydb`.`municipios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `estado_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_municipios_estado1_idx` (`estado_id` ASC) ,
  CONSTRAINT `fk_municipios_estado1`
    FOREIGN KEY (`estado_id`)
    REFERENCES `mydb`.`estados` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`direcciones`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`direcciones` ;

CREATE TABLE IF NOT EXISTS `mydb`.`direcciones` (
  `id` INT(40) NOT NULL AUTO_INCREMENT,
  `detalle` VARCHAR(45) NULL,
  `municipios_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_direcciones_municipios1_idx` (`municipios_id` ASC) ,
  CONSTRAINT `fk_direcciones_municipios1`
    FOREIGN KEY (`municipios_id`)
    REFERENCES `mydb`.`municipios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pacientes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`pacientes` ;

CREATE TABLE IF NOT EXISTS `mydb`.`pacientes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `direccion_actual` INT(40) NULL,
  `direccion_nacimiento` INT(40) NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `segundo_nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `segundo_apellido` VARCHAR(45) NULL,
  `documento` VARCHAR(12) NOT NULL,
  `sexo` ENUM('m', 'f', 'o') NULL,
  `fecha_nacimiento` DATE NULL,
  `estado_civil` ENUM('soltero', 'casado', 'divorciado', 'viudo') NULL,
  `tipo_sangre` ENUM('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-', 'DESCONOCIDO') NULL,
  `telefono` VARCHAR(20) NULL,
  `telefono2` VARCHAR(20) NULL,
  `img_url` VARCHAR(100) NULL DEFAULT 'N/A',
  `creado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `actualizado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `dir_actual1_idx` (`direccion_actual` ASC) ,
  INDEX `dir_nacimiento1_idx` (`direccion_nacimiento` ASC) ,
  UNIQUE INDEX `document_UNIQUE` (`documento` ASC) ,
  CONSTRAINT `dir_actual1`
    FOREIGN KEY (`direccion_actual`)
    REFERENCES `mydb`.`direcciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `dir_nacimiento1`
    FOREIGN KEY (`direccion_nacimiento`)
    REFERENCES `mydb`.`direcciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`usuarios`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`usuarios` ;

CREATE TABLE IF NOT EXISTS `mydb`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `contrasena` VARCHAR(200) NOT NULL,
  `rol` VARCHAR(45) NOT NULL,
  `titulo` VARCHAR(45) NULL,
  `documento` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NULL,
  `numero_colegio` VARCHAR(45) NULL,
  `numero_medico` VARCHAR(45) NULL,
  `sexo` ENUM('m', 'f', 'o') NULL,
  `fecha_nacimiento` DATE NULL,
  `activo` TINYINT NULL,
  `creado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `actualizado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `img_url` VARCHAR(200) NULL DEFAULT 'N/A',
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) ,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) ,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`historias_clinicas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`historias_clinicas` ;

CREATE TABLE IF NOT EXISTS `mydb`.`historias_clinicas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuarios_id` INT NOT NULL,
  `pacientes_id` INT NOT NULL,
  `motivo_consulta` VARCHAR(225) NOT NULL,
  `rasgos_cognitivos` VARCHAR(225) NOT NULL,
  `sistolica` INT(3) NOT NULL,
  `diastolica` INT(3) NOT NULL,
  `pulso` INT(3) NOT NULL,
  `freq_respiratoria` INT(3) NOT NULL,
  `temp` INT(3) NOT NULL,
  `diagnostico` VARCHAR(255) NULL,
  `ord_exam` VARCHAR(255) NULL,
  `exam_result` VARCHAR(45) NULL,
  `creado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `actualizado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_historias_clinicas_usuarios1_idx` (`usuarios_id` ASC) ,
  INDEX `fk_historias_clinicas_pacientes1_idx` (`pacientes_id` ASC) ,
  CONSTRAINT `fk_historias_clinicas_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `mydb`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_historias_clinicas_pacientes1`
    FOREIGN KEY (`pacientes_id`)
    REFERENCES `mydb`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`tipo_sintomas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`tipo_sintomas` ;

CREATE TABLE IF NOT EXISTS `mydb`.`tipo_sintomas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`tipo_profesiones`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`tipo_profesiones` ;

CREATE TABLE IF NOT EXISTS `mydb`.`tipo_profesiones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`tipo_examenes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`tipo_examenes` ;

CREATE TABLE IF NOT EXISTS `mydb`.`tipo_examenes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`examenes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`examenes` ;

CREATE TABLE IF NOT EXISTS `mydb`.`examenes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type_exam_id` INT NOT NULL,
  `entradas_id` INT NOT NULL,
  `resultado` VARCHAR(45) NULL,
  `date` VARCHAR(45) NULL,
  PRIMARY KEY (`id`, `entradas_id`),
  INDEX `fk_exam_result_type_exam1_idx` (`type_exam_id` ASC) ,
  INDEX `fk_examenes_entradas1_idx` (`entradas_id` ASC) ,
  CONSTRAINT `fk_exam_result_type_exam1`
    FOREIGN KEY (`type_exam_id`)
    REFERENCES `mydb`.`tipo_examenes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_examenes_entradas1`
    FOREIGN KEY (`entradas_id`)
    REFERENCES `mydb`.`historias_clinicas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`antecedentes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`antecedentes` ;

CREATE TABLE IF NOT EXISTS `mydb`.`antecedentes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`antecedentes_personales`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`antecedentes_personales` ;

CREATE TABLE IF NOT EXISTS `mydb`.`antecedentes_personales` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `antecedentes_id` INT NOT NULL,
  `pacientes_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_antecedentes_has_pacientes_pacientes1_idx` (`pacientes_id` ASC) ,
  INDEX `fk_antecedentes_has_pacientes_antecedentes1_idx` (`antecedentes_id` ASC) ,
  CONSTRAINT `fk_antecedentes_has_pacientes_antecedentes1`
    FOREIGN KEY (`antecedentes_id`)
    REFERENCES `mydb`.`antecedentes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_antecedentes_has_pacientes_pacientes1`
    FOREIGN KEY (`pacientes_id`)
    REFERENCES `mydb`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`antecedentes_familiares`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`antecedentes_familiares` ;

CREATE TABLE IF NOT EXISTS `mydb`.`antecedentes_familiares` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `pacientes_id` INT NOT NULL,
  `antecedentes_id` INT NOT NULL,
  `familiar` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pacientes_has_antecedentes_antecedentes1_idx` (`antecedentes_id` ASC) ,
  INDEX `fk_pacientes_has_antecedentes_pacientes1_idx` (`pacientes_id` ASC) ,
  CONSTRAINT `fk_pacientes_has_antecedentes_pacientes1`
    FOREIGN KEY (`pacientes_id`)
    REFERENCES `mydb`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pacientes_has_antecedentes_antecedentes1`
    FOREIGN KEY (`antecedentes_id`)
    REFERENCES `mydb`.`antecedentes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`profesiones`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`profesiones` ;

CREATE TABLE IF NOT EXISTS `mydb`.`profesiones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tipo_profesiones_id` INT NOT NULL,
  `pacientes_id` INT NOT NULL,
  `inicio` DATE NULL,
  `fin` DATE NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_profesiones_tipo_profesiones1_idx` (`tipo_profesiones_id` ASC) ,
  INDEX `fk_profesiones_pacientes1_idx` (`pacientes_id` ASC) ,
  CONSTRAINT `fk_profesiones_tipo_profesiones1`
    FOREIGN KEY (`tipo_profesiones_id`)
    REFERENCES `mydb`.`tipo_profesiones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_profesiones_pacientes1`
    FOREIGN KEY (`pacientes_id`)
    REFERENCES `mydb`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`tipo_vacunas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`tipo_vacunas` ;

CREATE TABLE IF NOT EXISTS `mydb`.`tipo_vacunas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`vacunas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`vacunas` ;

CREATE TABLE IF NOT EXISTS `mydb`.`vacunas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `pacientes_id` INT NOT NULL,
  `tipo_vacunas_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pacientes_has_tipo_vacunas_tipo_vacunas1_idx` (`tipo_vacunas_id` ASC) ,
  INDEX `fk_pacientes_has_tipo_vacunas_pacientes1_idx` (`pacientes_id` ASC) ,
  CONSTRAINT `fk_pacientes_has_tipo_vacunas_pacientes1`
    FOREIGN KEY (`pacientes_id`)
    REFERENCES `mydb`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pacientes_has_tipo_vacunas_tipo_vacunas1`
    FOREIGN KEY (`tipo_vacunas_id`)
    REFERENCES `mydb`.`tipo_vacunas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`sintomas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`sintomas` ;

CREATE TABLE IF NOT EXISTS `mydb`.`sintomas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `historias_clinicas_id` INT NOT NULL,
  `tipo_sintomas_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_historias_clinicas_has_tipo_sintomas_tipo_sintomas1_idx` (`tipo_sintomas_id` ASC) ,
  INDEX `fk_historias_clinicas_has_tipo_sintomas_historias_clinicas1_idx` (`historias_clinicas_id` ASC) ,
  CONSTRAINT `fk_historias_clinicas_has_tipo_sintomas_historias_clinicas1`
    FOREIGN KEY (`historias_clinicas_id`)
    REFERENCES `mydb`.`historias_clinicas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_historias_clinicas_has_tipo_sintomas_tipo_sintomas1`
    FOREIGN KEY (`tipo_sintomas_id`)
    REFERENCES `mydb`.`tipo_sintomas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`medicamentos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`medicamentos` ;

CREATE TABLE IF NOT EXISTS `mydb`.`medicamentos` (
  `id` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `principio_activo` VARCHAR(45) NOT NULL,
  `laboratorio` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`medicaciones`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`medicaciones` ;

CREATE TABLE IF NOT EXISTS `mydb`.`medicaciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `historias_clinicas_id` INT NOT NULL,
  `medicamentos_id` INT NOT NULL,
  `antecedente` TINYINT NULL,
  PRIMARY KEY (`id`, `historias_clinicas_id`, `medicamentos_id`),
  INDEX `fk_historias_clinicas_has_medicamentos_medicamentos1_idx` (`medicamentos_id` ASC) ,
  INDEX `fk_historias_clinicas_has_medicamentos_historias_clinicas1_idx` (`historias_clinicas_id` ASC) ,
  CONSTRAINT `fk_historias_clinicas_has_medicamentos_historias_clinicas1`
    FOREIGN KEY (`historias_clinicas_id`)
    REFERENCES `mydb`.`historias_clinicas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_historias_clinicas_has_medicamentos_medicamentos1`
    FOREIGN KEY (`medicamentos_id`)
    REFERENCES `mydb`.`medicamentos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`tipo_metadatos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`tipo_metadatos` ;

CREATE TABLE IF NOT EXISTS `mydb`.`tipo_metadatos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`metadatos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`metadatos` ;

CREATE TABLE IF NOT EXISTS `mydb`.`metadatos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `historias_clinicas_id` INT NOT NULL,
  `tipo_metadatos_id` INT NOT NULL,
  `relevante` TINYINT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_historias_clinicas_has_metadatos_metadatos1_idx` (`tipo_metadatos_id` ASC) ,
  INDEX `fk_historias_clinicas_has_metadatos_historias_clinicas1_idx` (`historias_clinicas_id` ASC) ,
  CONSTRAINT `fk_historias_clinicas_has_metadatos_historias_clinicas1`
    FOREIGN KEY (`historias_clinicas_id`)
    REFERENCES `mydb`.`historias_clinicas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_historias_clinicas_has_metadatos_metadatos1`
    FOREIGN KEY (`tipo_metadatos_id`)
    REFERENCES `mydb`.`tipo_metadatos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`conversaciones`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`conversaciones` ;

CREATE TABLE IF NOT EXISTS `mydb`.`conversaciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuarios_id` INT NOT NULL,
  `usuarios2_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_conversaciones_usuarios1_idx` (`usuarios_id` ASC) ,
  INDEX `fk_conversaciones_usuarios2_idx` (`usuarios2_id` ASC) ,
  CONSTRAINT `fk_conversaciones_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `mydb`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_conversaciones_usuarios2`
    FOREIGN KEY (`usuarios2_id`)
    REFERENCES `mydb`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`mensajes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`mensajes` ;

CREATE TABLE IF NOT EXISTS `mydb`.`mensajes` (
  `id` INT NOT NULL,
  `conversaciones_id` INT NOT NULL,
  `usuarios_id` INT NOT NULL,
  `contenido` VARCHAR(500) NOT NULL,
  `leido` TINYINT NOT NULL DEFAULT 0,
  `fecha` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_mensajes_conversaciones1_idx` (`conversaciones_id` ASC) ,
  INDEX `fk_mensajes_usuarios1_idx` (`usuarios_id` ASC) ,
  CONSTRAINT `fk_mensajes_conversaciones1`
    FOREIGN KEY (`conversaciones_id`)
    REFERENCES `mydb`.`conversaciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mensajes_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `mydb`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
