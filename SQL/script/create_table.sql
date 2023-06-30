
CREATE TABLE IF NOT EXISTS `usuario` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT unique,
  `nombre` VARCHAR(255) not null,
  `apellido` VARCHAR(255)not null,
   `email` Varchar(255) not null ,
    `contra` Varchar(255) not null,
    `tipo` int not null,
    `posicion` int default 0, 
    `borrado` int not null default 0,  
  PRIMARY KEY (id)
)  ENGINE = InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `video`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT unique,
    `nombre` VARCHAR(255) not null,
    PRIMARY KEY(id)
)ENGINE = InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `ejercicio` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT unique,
  `nombre` VARCHAR(255) not null,
  `descripcion` VARCHAR(255),
   `tiempo` int ,
    `tipo_tiempo` Varchar(255) ,
    `repeticiones` int,
    `tipo` int not null,
    `categoria` int not null,
    `video`  int unsigned not null ,
    `borrado` int not null default 0,
    `publico` int not null default 0,
    `entrenador`  int unsigned not null ,
  PRIMARY KEY (id),
  FOREIGN key(video)
    REFERENCES video(id)
    on UPDATE CASCADE
    on DELETE RESTRICT,
  FOREIGN key(entrenador)
    REFERENCES usuario(id)
    on UPDATE CASCADE
    on DELETE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `entrenamiento` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT unique,
  `nombre` VARCHAR(255) not null,
  `descripcion` VARCHAR(255),   
  `fecha` VARCHAR(255) not null,
  `borrado` int not null default 0,
  `entrenador` int unsigned not null,
  `tipo` int not null DEFAULT 0,
  PRIMARY KEY (id),
  FOREIGN key(entrenador)
    REFERENCES usuario(id)
    on UPDATE CASCADE
    on DELETE RESTRICT
)ENGINE = InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `ent_eje`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT unique,
    `ent` INT UNSIGNED NOT NULL,
    `eje` INT UNSIGNED NOT NULL,
    PRIMARY KEY(id),
   CONSTRAINT fk_ent FOREIGN KEY(ent) 
    	REFERENCES entrenamiento(id) 
    	ON UPDATE CASCADE 
    	ON DELETE RESTRICT,
    CONSTRAINT fk_eje FOREIGN KEY(eje) 
    	REFERENCES ejercicio(id) 
    	ON UPDATE CASCADE 
    	ON DELETE RESTRICT
)ENGINE = InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `ent_alu`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT unique,
    `ent` INT UNSIGNED NOT NULL,
    `alu` INT UNSIGNED NOT NULL,
    `coment_jug` Varchar(255),
    `asistencia` int not null DEFAULT 0,
    `nota` int unsigned ,
    `coment_ent` varchar(255),
    PRIMARY KEY(id), 
    FOREIGN KEY(ent) 
    	REFERENCES entrenamiento(id) 
    	ON UPDATE CASCADE 
    	ON DELETE RESTRICT,
    FOREIGN KEY(alu) 
    	REFERENCES usuario(id) 
    	ON UPDATE CASCADE 
    	ON DELETE RESTRICT
)ENGINE = InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `config`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT unique,
    `us` INT UNSIGNED NOT NULL,
    `tema`int not null default 1,
    PRIMARY KEY(id), 
    FOREIGN KEY(us) 
    	REFERENCES usuario(id) 
    	ON UPDATE CASCADE 
    	ON DELETE RESTRICT
)ENGINE = InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS `entrenador_alumno`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT unique,
    `entrenador` INT UNSIGNED NOT NULL,
    `alumno` INT UNSIGNED NOT NULl,
    PRIMARY KEY(id), 
    FOREIGN KEY(entrenador) 
    	REFERENCES usuario(id) 
    	ON UPDATE CASCADE 
    	ON DELETE RESTRICT,
    FOREIGN KEY(alumno) 
    	REFERENCES usuario(id) 
    	ON UPDATE CASCADE 
    	ON DELETE RESTRICT
)ENGINE = InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
