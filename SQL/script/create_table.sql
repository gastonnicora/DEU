
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

CREATE TABLE IF NOT EXISTS `notificacion` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT unique,
  `contenido` VARCHAR(255) not null,
  `entrenador` int unsigned not null,
  `fecha` timestamp default current_timestamp() on update current_timestamp(),
    `borrado` int not null default 0, 
  PRIMARY KEY (id),
  FOREIGN key(entrenador)
    REFERENCES usuario(id)
    on UPDATE CASCADE
    on DELETE RESTRICT
)ENGINE = InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `notificacion_alumno` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT unique,
  `notificacion` int unsigned not null,
  `alumno` int unsigned not null,
  `visto` int not null DEFAULT 0,
  PRIMARY KEY (id),
  FOREIGN key(alumno)
    REFERENCES usuario(id)
    on UPDATE CASCADE
    on DELETE RESTRICT,
  FOREIGN key(notificacion)
    REFERENCES notificacion(id)
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

INSERT INTO `usuario` (`id`, `nombre`, `apellido`, `email`, `contra`, `tipo`, `posicion`, `borrado`) VALUES
(1, 'Primer', 'Estudiante', 'estudiante1@gmail.com', '123456', 1, NULL, 0),
(2, 'Segundo', 'Estudiante', 'estudiante2@gmail.com', '123456', 1, NULL, 0),
(3, 'Unico', 'Entrenador', 'entrenador@gmail.com', '123456', 0, NULL, 0);

INSERT INTO `video` (`id`, `nombre`) VALUES
(1, 'b01f4d8e-9fe1-4cf7-aec5-42e80214e25e.mp4'),
(2, 'ec3ecdb3-fc36-4062-b091-c54f36729e81.mp4'),
(3, 'ff257496-f700-45ad-919c-e0016b4ebd6b.mp4'),
(4, 'be7a0ec1-cab2-439d-8140-a503135ab3cb.mp4');

INSERT INTO `config` (`id`, `us`, `tema`) VALUES
(3, 1, 1),
(4, 2, 1),
(5, 3, 1);

INSERT INTO `ejercicio` (`id`, `nombre`, `descripcion`, `tiempo`, `tipo_tiempo`, `repeticiones`, `tipo`, `categoria`, `video`, `borrado`, `publico`, `entrenador`) VALUES
(1, 'Flexión lateral', 'Párate con los pies separados a la altura de los hombros.\nLevanta tu mano derecha por encima de tu cabeza y flexiona tu cuerpo hacia el lado izquierdo, con la parte inferior y los músculos abdominales controlando el movimiento.\nAlterna entre el lado derec', 0, '', 15, 1, 0, 1, 0, 1, 3),
(2, 'Balanceo de piernas', 'Párate con los pies separados a la altura de los hombros y junto a una silla o pared para mantener el equilibrio.\nCon una mano apoyada en la silla/pared, balancea una pierna hacia delante y hacia atrás.\nTrata de mantener la parte superior del cuerpo viend', 1, '', 20, 1, 0, 2, 0, 1, 3),
(3, 'Estiramiento de los isquiotibiales', 'Recuéstate sobre la espalda con los pies apoyados frente a ti.\nLevanta la pierna derecha hacia ti y sostenla por la parte trasera con los dedos de ambas manos entrelazados.\nExhala mientras llevas la pierna hacia ti.\nMantén por 30 segundos.\nCambia de piern', 5, 'minutos', 1, 0, 2, 3, 0, 1, 3),
(4, 'Plancha', 'Mantén la parte superior de una flexión de brazos, con los hombros ubicados sobre las muñecas, la espalda plana (sin hundirse ni levantar las caderas), y abdominales, muslos y trasero contraídos. La mirada apunta unos centímetros hacia adelante de tus man', 1, '', 5, 1, 1, 4, 0, 1, 3);

INSERT INTO `entrenador_alumno` (`id`, `entrenador`, `alumno`) VALUES
(1, 3, 1);

INSERT INTO `entrenamiento` (`id`, `nombre`, `descripcion`, `fecha`, `borrado`, `entrenador`, `tipo`) VALUES
(1, 'Entrenamiento de fuerza', 'En este entrenamiento se va a entrenar el tren superior', '2023-07-31T19:23', 0, 3, 0),
(2, 'Entrenamiento de fuerza', 'En este entrenamiento se va a entrenar el tren superior', '2023-08-31T19:24', 0, 3, 0);

INSERT INTO `ent_alu` (`id`, `ent`, `alu`, `coment_jug`, `asistencia`, `nota`, `coment_ent`) VALUES
(1, 1, 1, NULL, 0, NULL, NULL),
(2, 2, 1, NULL, 0, NULL, NULL);

INSERT INTO `ent_eje` (`id`, `ent`, `eje`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 2, 1),
(6, 2, 3),
(7, 2, 4);

INSERT INTO `notificacion` (`id`, `contenido`, `entrenador`, `fecha`, `borrado`) VALUES
(1, 'Hola y bienvenido.  Cualquier consulta que tenga mande un email a: entrenador@gmail.com', 3, '2023-08-01 22:26:16', 0);


INSERT INTO `notificacion_alumno` (`id`, `notificacion`, `alumno`, `visto`) VALUES
(1, 1, 1, 0);

